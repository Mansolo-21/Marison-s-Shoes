from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('clothes', 'Clothes'),
        ('tshirts', 'T-Shirts'),
        ('trousers', 'Trousers'),
        ('jackets', 'Jackets'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.IntegerField()

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=20
    )

    image = CloudinaryField('image')

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    


class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=20)

    address = models.TextField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    mpesa_code = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    payment_confirmed = models.BooleanField(
        default=False
    )

    paid = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name
    