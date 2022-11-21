from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMEBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField()
    birth_date = models.DateTimeField(auto_now=False, null=True)
    membership = models.CharField(
        max_length=1, choices=MEMEBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE
    )


class Order(models.Model):

    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"

    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, "PENDING"),
        (PAYMENT_COMPLETE, "COMPLETE"),
        (PAYMENT_FAILED, "FAILED"),
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING
    )
