from django.urls import path , include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('',views.getRoute, name='getroutes'),
    path('item/',views.getItem,name='getitems'),
    path('suborder/',views.getSuborder,name='getsuborders'),
    path('suborder/create/',views.addSuborder,name='createsuborder')
]