from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from carts.models import Cart
from .models import Order, OrderItem


@login_required
def create_order(request):

    session_key = request.session.session_key

    cart = Cart.objects.filter(
        session_key=session_key
    ).first()

    if not cart:
        return redirect("carts:cart_detail")

    order = Order.objects.create(
        user=request.user,
        total_price=cart.total_price
    )

    for item in cart.items.all():

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart.items.all().delete()

    return redirect("orders:success")



#سفارش های من


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request,'order/my_orders.html',
        {
            "orders": orders
        }
    )

def order_success(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    return render(request, "order/order_success.html", {
        "order": order
    })