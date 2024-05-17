from django.shortcuts import render
from reservation.decorator import allowed_user
from django.views import View

class Dashboard(View):
    def get(self,request,*args,**kwargs):
        return render(request,'service/dashboard.html')

# Create your views here.
