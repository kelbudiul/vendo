from django.contrib import admin
from .models import Category, Product, Vendor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "parent"]
    prepopulated_fields = {
        "slug": (
            "name",
            "parent",
        )
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "vendor",
        "slug",
        "price",
        "availability",
        "created",
        "updated",
    ]
    list_filter = ["availability", "created", "updated", "vendor"]
    list_editable = ["price", "availability"]
    prepopulated_fields = {"slug": ("name", "vendor")}


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "contact_info",
        "billing_address",
        "registry_address",
        "registration_number",
        "joined_at",
    ]
