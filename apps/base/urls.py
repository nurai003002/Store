from django.urls import path
# from apps.secondary import views
from apps.base import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart1, name='add_to_cart'),
    
]
