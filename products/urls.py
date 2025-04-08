from django.urls import path

from products.views import (
    HomeListView,
    AboutTemplateView,
    ShopListView,
    ProductDetailView,
    CommentCreateView,
    WishlistListView,
    create_wishlist,
    CartView
)

app_name = 'products'

urlpatterns = [
    path('', HomeListView.as_view(), name='list'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', create_wishlist, name='wishlist-create'),
    path('cart/', CartView.as_view(), name='cart')
]
