from django.urls import path
from .views import *
urlpatterns=[
    path('',Dashboard.as_view(), name= 'dashboard'),
    path('item-list/',Item_List.as_view(),name='item-list'),
    path('update-item/<int:pk>',Update_Item.as_view(),name='update-item'),
    path('delete-item/<int:pk>',Delete_Item.as_view(),name='delete-item'),
    path('add-item/', Add_Item.as_view(), name='add-item'),
    path('add-person/', Add_person.as_view(), name='add-person')
]