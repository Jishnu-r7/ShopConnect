from django.db import models

# Create your models here.
class Item(models.Model):
    Item_Name=models.CharField(max_length=50)
    Item_Photo=models.ImageField(upload_to='static/images/')

class Shop_Item(models.Model):
    Shop_Id=models.IntegerField()
    Item_Id=models.IntegerField()
    Item_Quantity=models.IntegerField()
    Item_Count=models.IntegerField()
    Item_Quantity_Type=models.CharField(max_length=7)
    Item_Price=models.FloatField()    