from django.contrib import admin

from .models import CustomUser
# Register your models here.

class ModelAdminView(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, ModelAdminView)