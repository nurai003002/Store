from django.urls import path

from apps.products import views
urlpatterns = [
    path('shop/',views.shop, name='shop' ),
    path('shop_details/<int:id>/', views.shop_details, name='shop_details'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('news_detail/<int:id>/', views.news_detail, name='news_detail'),
    # path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('remove_from_wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

]
