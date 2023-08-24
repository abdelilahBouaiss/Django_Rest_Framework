from django.urls import path
from . import views
from rest_framework  import routers

router = routers.DefaultRouter()
router.register('address',views.CustomerAddressViewSet)
router.register('productrating',views.ProductRatingViewSet)

urlpatterns = [
    # Vendors
    path('vendors/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),
    # Products
    path('products/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    # Products catergory
    path('categories/', views.ProductCategoryList.as_view()),
    path('category/<int:pk>/', views.ProductCategoryDetail.as_view()),
    # Customers
    path('customers/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    # Orders
    path('orders/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    # OrdersItems
    # path('ordersItems/', views.OrderItemsList.as_view()),
    # path('orderItems/<int:pk>/', views.OrderItemsDetail.as_view()),
]

urlpatterns += router.urls