from django.contrib import admin
from .models import Product,Bid
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'user',
                    'minBidPrice', 'end_date']
    search_fields = ['title']
    list_filter = ['title','end_date', 'minBidPrice','user']
    list_per_page = 10



@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['product', 'user',
                    'bidAmount','created_at']
    search_fields = ['title']
    list_filter = ['product','created_at', 'user','bidAmount']
    list_per_page = 10


















    # actions = ['running','completed' ]
    
    # def running(self, request, queryset):
    #     for product in queryset:
    #         product.is_end_date =False
    #         product.save()

    # running.short_description = 'Running Auction'

    # def completed(self, request, queryset):
    #     for product in queryset:
    #         product.is_end_date =True
    #         product.save()

    # completed.short_description = 'Completed Auction'
