from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default='credit'  # Add a default value here
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    is_fraudulent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - ${self.amount}"