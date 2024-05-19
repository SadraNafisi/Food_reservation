from django.shortcuts import render
from reservation.decorator import allowed_user
from django.views import View
from reservation.models import Order
from django.utils import timezone
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

# Create your views here.
