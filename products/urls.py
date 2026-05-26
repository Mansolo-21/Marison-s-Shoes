from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('owner/add-product/', views.add_product, name='add_product'),
    path('checkout/', views.checkout, name='checkout'),
    path(
    'create-side-owner/',
    views.create_side_owner,
    name='create_side_owner'
),
path('orders',views.orders,name='orders')
]