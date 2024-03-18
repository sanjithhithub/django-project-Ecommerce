from django.contrib import admin
from .models import Product,Customer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'product_image']

@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','city','locality', 'state', 'zipcode']    
