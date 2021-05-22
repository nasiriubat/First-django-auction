from django.contrib import admin
from django.conf import settings
from .models import Account
# Register your models here.
#admin.site.register(Account)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']
    search_fields = ['email']
    list_filter = ['is_staff','is_active']
    list_per_page = 10


