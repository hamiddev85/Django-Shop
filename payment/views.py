from django.shortcuts import render, redirect
from carts.models import Cart
from order.models import Order, OrderItem


def payment_view(request):

    session_key = request.session.session_key
    cart = Cart.objects.filter(session_key=session_key).first()

    if not cart:
        return redirect("carts:cart_detail")

    items = cart.items.select_related("product")

    total_price = sum(i.total_price for i in items)

    return render(request, "payment/payment.html", {
        "cart": cart,
        "items": items,
        "total_price": total_price
    })



def payment_confirm(request):

    session_key = request.session.session_key
    cart = Cart.objects.filter(session_key=session_key).first()

    if not cart:
        return redirect("orders:order_success")

    items = cart.items.select_related("product")

    # ساخت Order
    order = Order.objects.create(
        user=request.user if request.user.is_authenticated else None,
        total_price=sum(i.total_price for i in items),
        is_paid=True
    )

    # ساخت OrderItems
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # پاک کردن سبد
    cart.items.all().delete()

    return redirect("orders:order_success", order_id=order.id)


