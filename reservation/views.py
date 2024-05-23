from django.shortcuts import render , redirect
from django.views import View
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user , allowed_user
from django.utils.decorators import method_decorator

def loginUser_unreachable(request,):
    if (request.user.is_authenticated):
        messages.info(request, 'you are already in your account.')
        return True
    else:
        return False
def context_order_items(request,items):
    """this method is because for showing what was
       the unconfirmed orders of customers if they
       have"""
    if unconfirmed_order := Order.objects.filter(is_confirm=False, customer=request.user):
        messages.info(request,"you did not confirm last "
                              "order . their amount can be seen in items below."
                              "also you could remove or confirm order in your orderlist.")
        suborders = SubOrder.objects.filter(order=unconfirmed_order[0])
        for suborder in suborders:
            items = items.exclude(pk=suborder.item.pk)
        context = {
            'items': items,
            'suborders': suborders
        }

    else:
        context = {
            'items': items
        }
    return context

class Index(View):
    def get(self,request,*args,**kwarg):
        items = Item.objects.all().order_by('-available',"type__name",'name')
        context= context_order_items(request,items)

        return render(request, 'reservation/index.html',context)

    def post(self, request, *args, **kwargs):
        '''it has a problem that in database should have only
            one unconfirmed order.'''
        total_item_amount = 0
        items = Item.objects.filter(available=True).order_by("type__name", 'name')
        unconfirmed_order = Order.objects.filter(customer=request.user,is_confirm=False)
        if not unconfirmed_order:
            order = Order.objects.create(customer=request.user)
        else:
            order=Order.objects.filter(customer=request.user,is_confirm=False)[0]

        for i in range(0, len(request.POST) - 1):
            chosen_item = items[i]
            try:
                item_amount = int(request.POST[f'{chosen_item.name}_amount'])
            except:
                messages.warning(request, f' {items[i]} not found')
                order.delete()
                return redirect('order-item')

            if(SubOrder.objects.filter(item=chosen_item, order=order)):
                if(item_amount!=0):
                    total_item_amount += item_amount
                    suborder = SubOrder.objects.filter(item=chosen_item, order=order)[0]
                    suborder.amount = item_amount
                    print(suborder)
                    suborder.save()
                else:
                    SubOrder.objects.filter(item=chosen_item, order=order).delete()
            else:
                if(item_amount!=0):
                    total_item_amount += item_amount
                    SubOrder.objects.create(item=chosen_item, amount=item_amount, order=order).save()
        if (total_item_amount == 0):
            messages.info(request, 'you did not choose any of these items')
            order.delete()
            return redirect('index')
        order.save()
        return redirect('order-check', pk=order.pk)
        #     if (int(item_amount) != 0):
        #         total_item_amount += 1
        #         if total_item_amount == 1 :
        #             if not unconfirmed_order:
        #                 order = Order.objects.create(customer=request.user).save()
        #             else:
        #                 order=Order.objects.filter(customer=request.user,is_confirm=False)[0]
        #
        #
        #         if(SubOrder.objects.filter(item=chosen_item, order=order)):
        #             SubOrder.objects.filter(item=chosen_item, order=order).amount = item_amount
        #         else:
        #             print(order)
        #             SubOrder.objects.create(item=chosen_item, amount=item_amount, order=order).save()
        #     elif unconfirmed_order and SubOrder.objects.filter(item=chosen_item , order=order):
        #         SubOrder.objects.filter(items=chosen_item , order=order).delete()
        # if (total_item_amount == 0):
        #     messages.info(request, 'you did not choose any of these items')
        #     return redirect('index')
        #
        # return redirect('order-check', pk=order.pk)


class IndexChoose(View):
    def get(self,request,*args,**kwargs):
        entry=request.GET.get('choices')
        choices= Item.objects.all().filter(
            Q(name__icontains=entry) | Q(type__name__contains=entry) | Q(price__icontains=entry)
        ).order_by('-available',"type__name",'name')
        context = context_order_items(request,choices)


        return render(request, 'reservation/index.html', context)


class Order_Item(View):
    @method_decorator(login_required(login_url='login'))
    def get(self,request,*args,**kwargs):
        items = Item.objects.filter(available=True).order_by("type__name",'name')

        context = {
            'items':items
        }
        return render(request, 'reservation/order.html', context)

    def post(self, request, *args, **kwargs):
        total_item_amount = 0
        items = Item.objects.filter(available=True).order_by("type__name", 'name')
        for i in range(0, len(request.POST) - 1):
            chosen_item = items[i]
            try:
                item_amount = request.POST[f'{chosen_item.name}_amount']
            except:
                messages.warning(request, f' {items[i]} not found')
                return redirect('order-item')

            if (int(item_amount) != 0):
                total_item_amount += 1
                if total_item_amount == 1:
                    order = Order.objects.create(customer=request.user)
                SubOrder.objects.create(item=chosen_item, amount=item_amount, order=order).save()
                print("helloll")

        if (total_item_amount == 0):
            messages.info(request, 'you did not choose any of these items')
            return redirect('order-item')

        # print(SubOrder.objects.filter(order=order))
        # context={
        #     'suborders':SubOrder.objects.filter(order=order),
        #     'order': order
        #
        # }
        return redirect('order-check', pk=order.pk)

        # if(len(suborders) == len(items)):
        #     for suborder in suborders:
        #         if suborder != 0:
        #             SubOrder.objects.create()
        # context={
        #
        # }
        # return render(request,'reservation/order-check.html',context)

class AboutUs(View):

    def get(self,request,*args,**kwargs):
        return render(request,'reservation/about-us.html')


class Signup_User(View):
    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        return render(request, 'reservation/signup.html')


    def post(self,request,*args,**kwargs):
        if loginUser_unreachable(request):
            return redirect('index')

        username= request.POST['username']
        password1= request.POST['password1']
        password2=request.POST['password2']
        email= request.POST['email']
        if(password1!=password2):
            messages.info(request, 'the passwords does not match')
            return redirect('signup')
        elif(User.objects.filter(Q(username__icontains=username))):
            messages.info(request,'this username is available. try another one')
            return redirect('signup')
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password1)
            new_user.save()
            return redirect('login')


class Login_User(View):
    @method_decorator(unauthenticated_user)
    def get(self,request,*args,**kwargs):
        return render(request,'reservation/login.html')

    def post(self,request,*args,**kwargs):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,f'you logged in successfully {user} ')
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect.')
            return redirect('login')

class Logout_User(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'you logged out successfully')
        return redirect('index')

class Order_Check(View):
    def get(self,request,pk,*args,**kwargs):
        order = Order.objects.filter(pk=pk)[0]
        suborders = SubOrder.objects.filter(order=order)
        # is_admin= request.user.groups.filter(name='admins',user=request.user)
        if(order.customer != request.user)and(not request.user.is_staff ):
            messages.warning(request,'you are not authorized to see this order detail.')
            return redirect('index')

        context={
            'suborders':suborders,
            'order':order
        }
        return render(request,'reservation/order-check.html',context)
        #return redirect('order-item')

class Order_List(View):
    @method_decorator(login_required(login_url='login'))
    def get(self,request,*args,**kwargs):
        orders=Order.objects.filter(customer=request.user)

        context={
            'orders': orders
        }

        return render(request, 'reservation/order-list.html', context)

# Create your views here.

class Order_list_All(View):
    @method_decorator(allowed_user(['admins','staffs']))
    def get(self,request,*args,**kwargs):
        orders=Order.objects.all()

        context = {
            'orders': orders
        }

        return render(request, 'reservation/order-list.html', context)

class Confirm_Order(View):
    def get(self,request,pk,*args,**kwargs):
        Order.objects.get(pk=pk).confirmed()
        print(Order.objects.get(pk=pk).is_confirm)
        return redirect('order-check',pk=pk)
class Delete_Order(View):
    def get(self,request,pk,*args,**kwargs):
        Order.objects.get(pk=pk).delete()
        messages.success(request,"your previous order deleted successfully.")
        return redirect('index')