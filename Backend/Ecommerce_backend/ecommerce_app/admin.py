from django.contrib import admin
from ecommerce_app.models import Product, Review, ProductImage, Tag, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Category)
