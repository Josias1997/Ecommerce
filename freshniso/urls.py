from django.urls import path
from .views import ItemDetailView, checkout, HomeView, add_to_cart, remove_from_cart, OrderSummaryView, remove_single_item_from_cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('checkout', checkout, name="checkout"),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)