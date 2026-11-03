from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):

    # USER
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # ORDER DETAILS
    item_name = models.CharField(max_length=100)

    quantity = models.IntegerField()

    delivery_option = models.CharField(max_length=50)

    address = models.TextField(
        blank=True,
        null=True
    )
    pickup_time = models.TimeField(
        null=True,
        blank=True
    )
    pickup_period = models.CharField(
        max_length=2,
        choices=[
            ('AM', 'AM'),
            ('PM', 'PM')
        ],
        blank=True,
        null=True
    )





    payment_method = models.CharField(max_length=50)

    # PAYMENT STATUS
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Success', 'Success'),
            ('Refunded', 'Refunded'),
        ],
        default='Pending'
    )

    # ORDER STATUS
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Processing', 'Processing'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending',
        verbose_name="Order Status"
    )

    ordered_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.item_name} - {self.user.username}"


class Staff(models.Model):

    username = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )

    password = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
        name = models.CharField(max_length=100)

        category = models.CharField(max_length=50)

        description = models.TextField()

        price = models.DecimalField(
            max_digits=10,
            decimal_places=2
        )

        image = models.URLField(
            blank=True,
            null=True
        )

        def __str__(self):
            return self.name