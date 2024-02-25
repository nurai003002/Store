from django.shortcuts import render, redirect, get_object_or_404

from apps.base.models import Settings,Slide,Collection,NewArrival,Card,Clients,News
from apps.secondary import models
from apps.products.models import Cart
def index(request):
    settings = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    collection = Collection.objects.all()
    new_arrival = NewArrival.objects.all()
    card = Card.objects.latest('id')
    clients = Clients.objects.latest('id')
    news = News.objects.latest('id')

    return render(request, 'base/index.html', locals())

# def add_to_cart1(request, product_id):
#     product = get_object_or_404(Card, pk=product_id)

#     card, created = Cart.objects.get_or_create(
#         title=product.title,
#         price=product.price, 
#         image=product.image,
#     )

#     return redirect('cart')


def about(request):
    settings = Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    team = models.Team.objects.latest('id')
    clients = Clients.objects.latest('id')

    return render(request, 'base/about.html', locals())


