from django.db import models
from django.contrib.auth.models import User  # For user authentication
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Vendor(models.Model):
    """"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendor_user")
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    registry_address = models.CharField(max_length=255)
    registration_number = models.CharField(
        max_length=255, unique=True, default=None, blank=True, null=True
    )
    logo = models.ImageField(upload_to="users/vendors/", blank=True)
    joined_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, unique=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        unique_together = (
            "slug",
            "parent",
        )
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return " -> ".join(full_path[::-1])

    def get_absolute_url(self):
        return reverse("inventory:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """"""

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.BooleanField(default=False)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=None
    )
    stock_quantity = models.PositiveIntegerField()
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="product",
    )
    category = models.ForeignKey(
        "Category", related_name="products", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("slug", "name", "category", "vendor")
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventory:product_detail", args=[self.id, self.slug])
