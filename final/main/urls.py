from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('product/<int:product_id>/', views.show_product, name='product'),
    path('product/success/', views.success, name='success_page'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    ]
