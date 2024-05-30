from django.shortcuts import render , redirect
from reservation.decorator import allowed_user
from django.views import View
from reservation.models import Order
from django.utils import timezone
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from reservation.models import Item , Food_Type
from django.contrib import messages


class Dashboard(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_user(['admins', 'staffs']))
    def get(self,request,*args,**kwargs):
        recent_orders= Order.objects.order_by("-order_date")[:4]
        today_order_amount = len(Order.objects.filter(order_date__date=date.today()))
        total_price = 0
        for order in Order.objects.filter(order_date__date=date.today()):
            total_price += order.total_price()
        today_total_income = total_price

        context={
            'recent_orders': recent_orders,
            "today_total_income": today_total_income,
            "today_order_amount": today_order_amount,
        }
        return render(request,'service/dashboard.html',context)

class Item_List(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_user(['admins', 'staffs']))
    def get(self,request,*args,**kwargs):
        items= Item.objects.all().order_by("type__name","name")

        context={
            'items':items
        }
        return render(request,'service/item-list.html',context)

class Update_Item(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_user(['admins', 'staffs']))
    def get(self,request,pk,*args,**kwargs):
        item=Item.objects.filter(pk=pk).get()
        types=Food_Type.objects.all()
        context={
            'item':item,
            'types':types
        }
        return render(request,'service/update-item.html',context)
    def post(self,request,pk,*args,**kwargs):
        item=Item.objects.filter(pk=pk).get()
        contents=request.POST
        print(bool(contents['clear']))
        if 'image' in request.FILES:
            if(contents['clear'] == 'True'):
                messages.warning(request,'there is only possible to'
                                         'clear the image or upload a new one.')
                return redirect(f'update-item',item.pk)
            item.image = request.FILES['image']
        if(contents['clear'] == 'True'):
            item.image.delete()
            item.image = None
        if item.name != contents['name']:
            item.name = contents['name']
        if item.price != contents['price']:
            item.price = int(contents['price'])
        if item.type != contents['type']:
            type=Food_Type.objects.filter(name=contents['type']).get()
            item.type = type
        if item.available != contents['available']:
            item.available = contents['available']

        item.save()
        return redirect('dashboard')


class Delete_Item(View):
    def get(self,request,pk,*args,**kwargs):
        item=Item.objects.filter(pk=pk).get()
        item.delete()
        messages.success(request,message=f'{item.name} item removed successfully')
        return redirect('item-list')

class Add_Item(View):
    def get(self,request,*args,**kwargs):
        types=Food_Type.objects.all()
        context={'types':types}
        return render(request,'service/add-item.html',context)

    def post(self,request,*args,**kwargs):
        content=request.POST

        type=Food_Type.objects.filter(name=content['type']).get()
        item=Item.objects.create(name=content['name'],type=type,available=content['available'])
        print(content['price'])
        if content['price']:
            item.price=int(content['price'])
        if 'image' in request.FILES:
            item.image = request.FILES['image']
        item.save()
        messages.success(request,'the item created successfully!')
        return redirect('item-list')

# Create your views here.
