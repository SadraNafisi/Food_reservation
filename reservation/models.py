from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    name = models.CharField(max_length=64,unique=True)
    image = models.ImageField(upload_to="item_images/",blank=True)
    price = models.DecimalField(max_digits=8 , decimal_places=0,blank=True)
    type = models.ForeignKey("Food_Type", on_delete=models.RESTRICT)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Food_Type(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name

class SubOrder(models.Model):
    item = models.ForeignKey('Item',on_delete=models.CASCADE)
    amount = models.IntegerField()
    order = models.ForeignKey('Order',on_delete=models.CASCADE)
    def __str__(self):
        return f' {self.item.name}(order{self.order.pk})'
    def suborder_price (self):
        return self.amount * self.item.price
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.RESTRICT)
    order_date = models.DateTimeField("Order date",auto_now_add=True) ##add this in final changes

    def __str__(self):
        return  f'order{self.pk}'

    def total_price(self):
        total_price=0
        suborders= SubOrder.objects.filter(order=self.pk)
        for suborder in suborders:
           total_price +=suborder.item.price * suborder.amount

        return total_price



# Create your models here.
