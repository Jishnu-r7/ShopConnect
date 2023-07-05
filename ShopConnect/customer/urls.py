from django.urls import path
from customer import views

urlpatterns=[
    path('',views.custhome,name='custhome'),
    path('shoppage',views.shoppage,name='shoppage'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cart,name='cart'),
    path('clear_cart',views.clear_cart,name='clear_cart'),
    path('edit_user_item',views.edit_user_item,name='edit_user_item'),
    path('buyitems',views.buyitems,name='buyitems'),
    path('orders',views.orders,name='orders'),
    path('custorderdetails',views.custorderdetails,name='custorderdetails'),
    path('custfeedback',views.custfeedback,name='custfeedback')
]