from django.shortcuts import render

from apps.secondary import models
from apps.base.models import Settings,Clients
# Create your views here.

def about(request):
    settings = Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    team = models.Team.objects.latest('id')
    clients = Clients.objects.latest('id')

    return render(request, 'base/about.html', locals())
# Create your views here.
def team(request):
    settings = Settings.objects.latest('id')
    team = models.Team.objects.latest('id')
    employee = models.Employee.objects.all()
    return render(request, 'secondary/team.html', locals())

def team_detail(request, id):
    settings = Settings.objects.latest('id')
    employee = models.Employee.objects.get(id=id)
    return render(request, 'secondary/team-single.html',locals())