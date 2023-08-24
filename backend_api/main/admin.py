from django.contrib import admin
from . import models


# Vendor
admin.site.register(models.Vendor)

# Category
admin.site.register(models.ProductCategory)

# Product
admin.site.register(models.Product)

# Costumer
admin.site.register(models.Customer)

# Order
admin.site.register(models.Order)

# OrderItems
# admin.site.register(models.OrderItems)

# CustomerAddress
admin.site.register(models.CustomerAddress)

# ProductRating
admin.site.register(models.ProductRating)

