from django.contrib import admin
from .models import Category, Product, OrderUser

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)


# class ProductInline(admin.TabularInline):
#     model = Product


class ProductInline(admin.StackedInline):
    model = Product.user.through
    extra = 1


class OrderUserAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = ['user_name', 'email', 'product_id']


admin.site.register(OrderUser, OrderUserAdmin)

