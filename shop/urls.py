from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='procatdetail')
]
