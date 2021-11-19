from django import contrib
from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from Reading.models import ReadingBook, Category, QuesModel

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ReadingBook)
class ReadBookAdmin(admin.ModelAdmin):
    list_display = ('name','content_reading')
    search_fields = ('name',)
    
@admin.register(QuesModel)
class QuesMoldelAdmin(admin.ModelAdmin):
    list_display = ('question','name_read',)
