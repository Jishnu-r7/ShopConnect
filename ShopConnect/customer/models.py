from django.db import models
import datetime
# Create your models here.

class Bill(models.Model):
    Cust_Id=models.IntegerField()
    Shop_Id=models.IntegerField()
    Cust_House=models.CharField(max_length=50)
    Cust_Road=models.CharField(max_length=50)
    Cust_Locality=models.CharField(max_length=50)
    Cust_Dist=models.CharField(max_length=50)
    Total_Price=models.FloatField()
    date = models.DateField (default=datetime.datetime.today)
    Item_Delivered=models.CharField(max_length=1)

class Bill_Items(models.Model):
    Bill_Id=models.IntegerField()
    Item_Id=models.IntegerField()
    Item_Name=models.CharField(max_length=50)
    Item_Quantity=models.IntegerField()
    Item_Quantity_Type=models.CharField(max_length=7)
    Item_Count=models.IntegerField()
    Item_Price=models.IntegerField()

class Cart(models.Model):
    Cust_Id=models.IntegerField()
    Shop_Id=models.IntegerField()
    Item_Id=models.IntegerField()
    Item_Quantity=models.IntegerField()
    Item_Quantity_Type=models.CharField(max_length=7)
    Item_Price=models.FloatField()
    Item_Count=models.IntegerField()
    
class Feedback(models.Model):
    Cust_Id=models.IntegerField()
    Shop_Id=models.IntegerField()
    Satisfaction=models.CharField(max_length=10)
    Comment=models.TextField()
    Cust_Name=models.TextField()
    