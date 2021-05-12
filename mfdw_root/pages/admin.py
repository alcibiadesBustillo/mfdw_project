from django.contrib import admin
from django.urls.conf import include
from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)
admin.site.register(Page, PageAdmin)