# Generated by Django 5.0.1 on 2024-01-12 03:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0010_alter_product_vendor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="order",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="product",
        ),
        migrations.RemoveField(
            model_name="paymentmethod",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="review",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="review",
            name="product",
        ),
        migrations.RemoveField(
            model_name="shippingaddress",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="shoppingcart",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="wishlist",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="wishlistitem",
            name="wishlist",
        ),
        migrations.RemoveField(
            model_name="wishlistitem",
            name="product",
        ),
        migrations.DeleteModel(
            name="CartItem",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderItem",
        ),
        migrations.DeleteModel(
            name="PaymentMethod",
        ),
        migrations.DeleteModel(
            name="Review",
        ),
        migrations.DeleteModel(
            name="ShippingAddress",
        ),
        migrations.DeleteModel(
            name="ShoppingCart",
        ),
        migrations.DeleteModel(
            name="Wishlist",
        ),
        migrations.DeleteModel(
            name="WishlistItem",
        ),
    ]