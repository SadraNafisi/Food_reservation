import datetime

from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    name = models.CharField(max_length=64,unique=True)
    image = models.ImageField(upload_to="item_images/",blank=True)
    price = models.DecimalField(max_digits=8 , decimal_places=0,blank=True,default=0)
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
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    order_date = models.DateTimeField("Order date",auto_now_add=True) # add this in final changes
    is_confirmed = models.BooleanField(db_default=True, default=False)
    suborders = models.JSONField(default=list)
    items = models.JSONField(default=list)

    def __str__(self):
        return f'Order {self.pk}'

    def save(self, *args, **kwargs):
        if self.is_confirmed:
            self.suborders = [
                {
                    'item_name': suborder.item.name,
                    'amount': suborder.amount,
                    'item_price': int(suborder.item.price),
                    'suborder_price': int(suborder.item.price*suborder.amount)
                }
                for suborder in SubOrder.objects.filter(order=self)
            ]
            self.items = [
                {
                    'name': item.name,
                    'price': int(item.price),
                }
                for item in Item.objects.filter(suborder__order=self)
            ]
        super().save(*args, **kwargs)

    def total_price(self):
        if not self.is_confirmed:
            return sum(suborder.item.price * suborder.amount for suborder in self.suborder_set.all())
        else:
            return sum(suborder['item_price'] * suborder['amount'] for suborder in self.suborders)
    def confirm(self):
        self.is_confirmed = True
        self.save()

# Create your models here.