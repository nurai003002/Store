from django.urls import path
# from apps.secondary import views
from apps.base import views
from apps.secondary.views import team, team_detail

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart1, name='add_to_cart'),
    path('team/', team, name='team'),
    path('team/<int:id>/',team_detail, name='team_detail'),
    
]
