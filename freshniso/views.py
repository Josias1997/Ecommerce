from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone

# Create your views here.


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "freshniso/product.html", context)


def checkout(request):
    return render(request, "freshniso/checkout.html")


class HomeView(ListView):
    model = Item
    template_name = 'freshniso/home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'freshniso/product.html'


def add_to_cart(request, slug):
    item = Item.objects.get(slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
    return redirect("product", slug=slug)
