from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Index.as_view(), name="index"),
    # path('order-item/', Order_Item.as_view(), name='order-item'), #deleted
    path('About-us/', AboutUs.as_view(), name='about-us'),
    path('indexChoose/', IndexChoose.as_view(), name='index-choose'),
    path('signup/', Signup_User.as_view(), name='signup'),
    path('login/', Login_User.as_view(), name='login'),
    path('logout/', Logout_User.as_view(), name='logout'),
    path('order-check/<pk>/',Order_Check.as_view(),name="order-check"),
    path('order-list/',Order_List.as_view(), name='order-list'),
    path('order-list-all',Order_list_All.as_view(),name='order-list-all'),
    path('order-confirm/<int:pk>',Confirm_Order.as_view(),name='order-confirm'),
    path('order-delete/<int:pk>',Delete_Order.as_view(),name='order-delete'),
    path('current-unconfirmed-suborders/',View_Unconfirmed_Suborders.as_view()
         ,name='current-unconfirmed-suborders'),
]
