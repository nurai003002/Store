from django.shortcuts import render

from apps.secondary import models
from apps.base.models import Settings,Slide
# Create your views here.

def team(request):
    title = "Команда"
    slide = Slide.objects.all()
    settings = Settings.objects.latest('id')
    team = models.Team.objects.latest('id')
    
    return render(request, 'secondary/team.html', locals())

def team_detail(request, id):
    title = "Команда"
    slide = Slide.objects.all()
    settings = Settings.objects.latest('id')
    team = models.Team.objects.latest('id')
    team_details = models.Team.objects.get(id=id)
    
    return render(request, 'secondary/team-single.html',locals())

def faq(request):
    title = "FAQ"
    slide = Slide.objects.latest('id') 
    settings = Settings.objects.latest('id')
    faq = models.Faq.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_comment = request.POST.get('comment')

        new_comment = models.Review(name=name, email=email, comment=user_comment)
        new_comment.save()

        faq.comments.add(new_comment)
    return render(request, 'service/faq.html', locals())


def page_not_found(request):
    title = "404"
    slide = Slide.objects.latest('id') 
    settings = Settings.objects.latest('id')
    return render(request, '404.html', locals())