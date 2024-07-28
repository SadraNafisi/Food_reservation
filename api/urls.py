from django.urls import path , include
from . import views
urlpatterns=[
    path('',views.getRoute, name='getroutes'),
    path('item/',views.getItem,name='getitems'),
    path('suborder/',views.getSuborder,name='getsuborders'),
]