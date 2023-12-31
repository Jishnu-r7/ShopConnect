# Generated by Django 4.2.2 on 2023-06-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=50)),
                ('Item_Photo', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Id', models.IntegerField()),
                ('Item_Quantity', models.IntegerField()),
                ('Item_Quantity_Type', models.CharField(max_length=7)),
                ('Item_Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shop_Id', models.IntegerField()),
                ('Item_Id', models.IntegerField()),
                ('Item_Quantity', models.IntegerField()),
                ('Item_Count', models.IntegerField()),
                ('Item_Quantity_Type', models.CharField(max_length=7)),
            ],
        ),
    ]
