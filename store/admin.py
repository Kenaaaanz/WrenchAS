from django.contrib import admin
from .models import Vendor, Address, Category, Product, Cart, Order

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user', 'is_approved', 'shipping_status')
    list_filter = ('is_approved', 'shipping_status')
    search_fields = ('store_name', 'user__username', 'user__email')
    actions = ['approve_vendors']

    def approve_vendors(self, request, queryset):
        queryset.update(is_approved=True)
    approve_vendors.short_description = "Approve selected vendors"

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('locality', 'city', 'state')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'price', 'is_active', 'is_featured')
    list_filter = ('vendor', 'is_active', 'is_featured')
    search_fields = ('title', 'sku', 'vendor__store_name')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user__username', 'product__title')


admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)

