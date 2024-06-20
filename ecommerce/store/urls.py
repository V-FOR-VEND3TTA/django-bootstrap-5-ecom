from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('categories/', views.category_overview, name='category_overview'),
    path('category/<int:category_id>/', views.category_page, name='category_page'),
    path('product/<int:product_id>/', views.product_page, name='product_page'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('account/', views.account, name='account'),
]
