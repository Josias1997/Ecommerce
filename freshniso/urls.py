from django.urls import path
from .views import ItemDetailView, checkout, HomeView, add_to_cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/<slug>/', ItemDetailView.as_view(), name="product"),
    path('checkout', checkout, name="checkout"),
    path('', HomeView.as_view(), name="home"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
