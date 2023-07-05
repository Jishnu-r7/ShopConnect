from django.db import models

# Create your models here.
class Customer(models.Model):
    Cust_Name=models.CharField(max_length=50)
    Cust_Mail=models.CharField(max_length=50)
    Cust_Phone=models.CharField(max_length=10)
    Cust_Pass=models.CharField(max_length=50)
    Cust_House=models.CharField(max_length=50)
    Cust_Road=models.CharField(max_length=50)
    Cust_Locality=models.CharField(max_length=50)
    Cust_Dist=models.CharField(max_length=50)


class Shop_Owner(models.Model):
    Shop_Name=models.CharField(max_length=50)
    Shop_Mail=models.CharField(max_length=50)
    Shop_Owner_Name=models.CharField(max_length=50)
    Shop_Phone=models.CharField(max_length=10)
    Shop_Pass=models.CharField(max_length=50)
    Shop_Road=models.CharField(max_length=50)
    Shop_Locality=models.CharField(max_length=50)
    Shop_Dist=models.CharField(max_length=50)

