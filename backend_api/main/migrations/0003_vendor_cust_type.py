# Generated by Django 4.2.4 on 2023-08-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_productcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='cust_type',
            field=models.TextField(default='null'),
        ),
    ]
