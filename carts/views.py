from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem, Cart
# ویو نمایش سبد خرید

def cart_detail(request):

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    cart = Cart.objects.filter(
        session_key=session_key
    ).first()

    cart_items = []
    total_price = 0

    if cart:
        cart_items = cart.items.select_related('product')

        total_price = sum(
            item.total_price
            for item in cart_items
        )

    return render(
        request,
        'carts/cart_detail.html',
        {
            'cart': cart,
            'cart_items': cart_items,
            'total_price': total_price
        }
    )


# ویو افزودن محصول به سبد خرید
def add_to_cart(request, product_id):

    # گرفتن محصول
    product = get_object_or_404(
        Product,
        id=product_id
    )

    # ساخت session در صورت نبودن
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    # گرفتن یا ساخت سبد خرید
    cart, created = Cart.objects.get_or_create(
        session_key=session_key
    )

    # گرفتن یا ساخت آیتم سبد
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    # اگر از قبل وجود داشت تعداد را زیاد کن
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('carts:cart_detail')




# ویو حذف یک آیتم از سبد خرید
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id
    )

    item.delete()


    return redirect('carts:cart_detail')
