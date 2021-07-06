from django.contrib import admin

from main.models import Product, Bill, ProductImage


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class AdminProductDisplay(admin.ModelAdmin):
    readonly_fields = ('slug', )
    fields = ('slug', 'title', 'des', 'count_bill')
    search_fields = ('title', )
    inlines = (ProductImageInLine, )


@admin.register(Bill)
class AdminBillDisplay(admin.ModelAdmin):
    pass

