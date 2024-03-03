from django.shortcuts import render

from apps.secondary import models
from apps.base.models import Settings,Clients,Slide
# Create your views here.

def about(request):
    settings = Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    team = models.Team.objects.latest('id')
    clients = Clients.objects.latest('id')

    return render(request, 'base/about.html', locals())

def team(request):
    slide = Slide.objects.all()
    settings = Settings.objects.latest('id')
    team = models.Team.objects.latest('id')
    
    return render(request, 'secondary/team.html', locals())

def team_detail(request, id):
    slide = Slide.objects.all()
    settings = Settings.objects.latest('id')
    team = models.Team.objects.latest('id')
    team_details = models.Team.objects.get(id=id)
    
    return render(request, 'secondary/team-single.html',locals())

def faq(request):
    slide = Slide.objects.latest('id') 
    settings = Settings.objects.latest('id')
    faq = models.Faq.objects.all()
    return render(request, 'service/faq.html', locals())