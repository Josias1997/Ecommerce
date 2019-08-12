from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm


# Create your views here.


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "freshniso/product.html", context)


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, "freshniso/checkout.html", context)

    def post(self):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print("The form is valid")
            return redirect("checkout")


class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'freshniso/home.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
        return render(self.request, 'freshniso/order_summary.html', {'order': order})


class ItemDetailView(DetailView):
    model = Item
    template_name = 'freshniso/product.html'


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "You item was updated")
        else:
            messages.info(request, "You item was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "You item was added to your cart")
    return redirect("order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            order.save()
            messages.info(request, "You item was removed from your cart")
        else:
            messages.info(request, "You item was not in your cart")
    else:
        messages.info(request, "You do not have an active order")

    return redirect("product", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity <= 1:
                order.items.remove(order_item)
            else:
                order_item.quantity -= 1
                order_item.save()
            messages.info(request, "You item quantity was decreased")
        else:
            messages.info(request, "You item was not in your cart")
    else:
        messages.info(request, "You do not have an active order")

    return redirect("order-summary")
