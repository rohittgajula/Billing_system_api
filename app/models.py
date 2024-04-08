from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True, default="")
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_amount(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return str(Customer.name)

