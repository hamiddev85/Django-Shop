from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
        path('', views.home, name='home'),

        path('category/<slug:slug>/',views.category_products,name='category_products'),

        path('product/<slug:slug>/',views.product_detail,name='product_detail'),

        path('about/', views.about, name='about'),

        path("search/",views.search_products,name="search_products"),
]