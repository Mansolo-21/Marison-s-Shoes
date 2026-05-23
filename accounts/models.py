from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):

    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('side_owner', 'Side Owner'),
        ('owner', 'Owner'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='customer'
    )

    avatar = CloudinaryField(
        'image',
        blank=True,
        null=True
    )

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @property
    def is_owner(self):
        return self.role == "owner"

    @property
    def is_side_owner(self):
        return self.role == "side_owner"

    @property
    def is_customer(self):
        return self.role == "customer"