from django.urls import path
from owner import views

urlpatterns=[
    path('',views.ownerhome,name='ownerhome'),
    path('owner_add_item',views.owner_add_item,name='owner_add_item'),
    path('edit_shop_item',views.edit_shop_item,name='edit_shop_item'),
    path('submit_existing_item',views.submit_existing_item,name='submit_existing_item'),
    path('ownerorders',views.ownerorders,name='ownerorders'),
    path('ordedetails',views.orderdetails,name='orderdetails'),
    path('deliver',views.deliver,name='deliver'),
    path('logout',views.logout,name='logout'),
    path('ownerfeedback',views.ownerfeedback,name='ownerfeedback')
]