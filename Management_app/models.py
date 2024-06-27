from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zipcode}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    manager = models.CharField(max_length=100)

    def __str__(self):
        return self.manager

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    lifetime = models.IntegerField()

    def __str__(self):
        return self.name

class Stock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.manager}"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class Delivery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    priority = models.CharField(max_length=50, choices=[('prime', 'Prime'), ('regular', 'Regular')])

    def __str__(self):
        return f"Delivery {self.id} to {self.location.address}"

