from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from apps.base import models
from apps.secondary.models import About
from apps.products.models import Goods, Cart, Wishlist

# Create your views here.

def shop(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    about = About.objects.latest('id')  
    goods = Goods.objects.all()
    paginator = Paginator(goods, 3)  # Пагинация по трем товарам на странице
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/shop.html', locals())


def add_to_cart(request, product_id):
    product = Cart.objects.all()
    product_item = get_object_or_404(Cart, pk=product_id)

    return redirect('products/cart')


def shop_details(request, id):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    about = About.objects.latest('id')
    goods = Goods.objects.all()
    new_arrival = models.NewArrival.objects.all()
    goods_details = Goods.objects.get(id=id)

    return render(request, 'products/shop-details.html', locals())

def cart(request):
    about = About.objects.latest('id')  
    goods = Goods.objects.all()
    cart_items = Cart.objects.all()
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    
    return render(request, 'products/cart.html', locals())


def wishlist(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    wiahlist_items = Wishlist.objects.all()
    return render(request, 'products/wishlist.html', locals())

def add_to_cart(request, product_id):
    # Получаем продукт по его ID
    product = get_object_or_404(Goods, pk=product_id)

    # Создаем объект корзины с данными о продукте
    cart_item, created = Cart.objects.get_or_create(
        title=product.title,
        price=product.new_price,  # Используем цену из поля new_price продукта
        image=product.image,
    )

    # После добавления продукта в корзину перенаправляем пользователя на страницу корзины
    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')


# wishlist
def add_to_wishlist(request, product_id):
    # Получаем продукт по его ID
    product = get_object_or_404(Goods, pk=product_id)

    # Создаем объект корзины с данными о продукте
    wishlist_item, created = Cart.objects.get_or_create(
        title=product.title,
        price=product.new_price,  # Используем цену из поля new_price продукта
        image=product.image,
    )

    # После добавления продукта в корзину перенаправляем пользователя на страницу корзины
    return redirect('wishlist')

def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(Cart, pk=wishlist_item_id)
    wishlist_item.delete()
    return redirect('wishlist')