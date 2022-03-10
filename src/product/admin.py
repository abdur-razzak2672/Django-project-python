from django.contrib import admin
from .models import *

admin.site.register(Variant)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)
