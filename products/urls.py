from django.urls import path
from .views import list_products, create_product, update_product, delete_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_product, name='create_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
]


# CRUD - CREATE, READ, UPDATE, DELETE