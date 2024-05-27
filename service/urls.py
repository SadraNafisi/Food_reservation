from django.urls import path
from .views import *

urlpatterns=[
    path('',Dashboard.as_view(), name= 'dashboard'),
    path('item-list/',Item_List.as_view(),name='item-list')

]