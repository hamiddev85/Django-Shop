from django.shortcuts import render, redirect

from carts.models import Cart
from .forms import ProductForm
from .models import Category, Product

def home(request):
    categories = Category.objects.all()

    products = Product.objects.filter(
        is_available=True
    )

    query = request.GET.get("q")

    if query:
        products = products.filter(
            name__icontains=query
        )


    suggested_products = Product.objects.filter(
        is_available=True
    ).order_by('?')[:8]

    cart_count = 0

    if request.session.session_key:
        cart = Cart.objects.filter(
            session_key=request.session.session_key
        ).first()

        if cart:
            cart_count = sum(
                item.quantity
                for item in cart.items.all()
            )

    return render(request, 'products/home.html', {
        'categories': categories,
        'products': products,
        'suggested_products': suggested_products,
        'cart_count': cart_count
    })


def search_products(request):

    query = request.GET.get("q", "").strip()

    products = Product.objects.none()

    if query:
        products = Product.objects.filter(
            name__icontains=query,
            is_available=True
        )

    return render(
        request,
        "products/search_results.html",
        {
            "products": products,
            "query": query
        }
    )

def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category, is_available=True)

    return render(request, 'products/category_products.html', {
        'category': category,
        'products': products
    })




def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    return render(request, 'products/product_detail.html', {
        'product': product
    })



def about(request):
    return render(request, "products/about.html")