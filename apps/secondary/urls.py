from django.urls import path

from apps.secondary.views import team,team_detail, faq,page_not_found

urlpatterns = [
    path('team/', team, name='team'),
    path('team_detail/<int:id>/',team_detail, name='team_detail'),
    path('faq/', faq, name='faq'),
    path('page_not_found/', page_not_found, name='page_not_found'),
    
]

