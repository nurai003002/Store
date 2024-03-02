from django.urls import path

from apps.secondary.views import team,team_detail

urlpatterns = [
    path('team/', team, name='team'),
    path('team_detail/<int:id>/',team_detail, name='team_detail'),
    
]

