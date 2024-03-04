from django.shortcuts import render

from apps.base.models import Settings,Slide
from apps.contacts import models
from apps.telegram_bot.views import get_text
# Create your views here.

def contacts(request):
    title = "Контакты"
    settings = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')

    if request.method=='POST':
        if "newslater" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            page_contact = models.Contacts.objects.create(name=name, email=email, phone=phone, message=message)
            if page_contact:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                                
        Имя пользователя:  {name}
        Почта: {email}
        Номер телефона: {phone}
        Сообщение: {message}

        """)
  
    return render(request, 'base/contact.html', locals())

