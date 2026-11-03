from django.contrib import admin
from .models import Order, Staff, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'description',
        'price'
    )

# 👨‍🍳 STAFF ADMIN
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'position'
    )


# 📦 ORDER ADMIN (UPDATED)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'item_name',
        'quantity',
        'delivery_option',
        'address',
        'pickup_time',
        'pickup_period',
        'payment_method',
        'payment_status',
        'status',
        'ordered_at'
    )

    list_filter = (
        'payment_status',
        'status',
        'delivery_option',
        'payment_method'
    )

    search_fields = (
        'user__username',
        'item_name',
        'payment_method'
    )

    ordering = ('-ordered_at',)

    list_editable = (
        'payment_status',
        'status',
    )