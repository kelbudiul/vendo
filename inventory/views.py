from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(parent=None)
    products = Product.objects.filter(availability=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "inventory/product/list.html",
        {"category": category, "categories": categories, "products": products},
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, availability=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "inventory/product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )



# Stripe provides different test credit cards from different card issuers and countries, which allows you 
# to simulate payments to test all possible scenarios (successful payment, declined payment, etc.). The 
# following table shows some of the cards you can test for different scenarios:
# Result Test Credit Card CVC Expiry date
# Successful payment 4242 4242 4242 4242 Any 3 digits Any future date
# Failed payment 4000 0000 0000 0002 Any 3 digits Any future date
# Requires 3D secure 
# authentication
# 4000 0025 0000 3155 Any 3 digits Any future date