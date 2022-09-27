from django.contrib import admin
from .models import Category, Taglines, ItemListing

# Register your models here.

admin.site.register(ItemListing)
admin.site.register(Category)
admin.site.register(Taglines)

