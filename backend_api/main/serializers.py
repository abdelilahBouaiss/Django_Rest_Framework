from rest_framework import serializers
from . import models

########################
## Vendor related Class
########################

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user','address','cust_type']

    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user','address','cust_type']

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

########################
## Product related Class
########################

class ProductListSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title', 'detail', 'price', 'product_ratings']

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class ProductDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Product
        fields = ['id','category','vendor','title','detail','price', 'product_ratings']

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

#################################
## Product Category related Class
#################################

class ProductCategorySerializer(serializers.ModelSerializer):
    #product_ratings = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.ProductCategory
        fields = ['id', 'title', 'detail']

    def __init__(self, *args, **kwargs):
        super(ProductCategorySerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class ProductCategoryDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ProductCategory
        fields = ['id','title', 'detail']
    def __init__(self, *args, **kwargs):
        super(ProductCategoryDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

########################
## Customer related Class
########################

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user','address','cust_type','mobile_no']

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user','address','cust_type','mobile_no']

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

########################
## Order related Class
########################

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id','customer','order_time']

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

"""
    - Order related Items List Method 
"""
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['id','order', 'product']

    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

###########################
## OrderItems related Class
###########################

# class OrderItemsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.OrderItems
#         fields = ['id', 'order', 'product']

#     def __init__(self, *args, **kwargs):
#         super(OrderItemsSerializer, self).__init__(*args, **kwargs)
#         self.Meta.depth = 1

# class OrderItemsDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.OrderItems
#         fields = ['id', 'order', 'product']

#     def __init__(self, *args, **kwargs):
#         super(OrderItemsDetailSerializer, self).__init__(*args, **kwargs)
#         self.Meta.depth = 1

#################################
## Customer Address related Class
#################################

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id','customer','address','default_address']

    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

###############################
## Product Rating related Class
###############################

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ['id','customer', 'product', 'rating', 'reviews', 'add_time']

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1