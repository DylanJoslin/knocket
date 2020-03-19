from django.contrib import admin
from .models import VideoPost, Category, School
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(School, CategoryAdmin)
admin.site.register(VideoPost)