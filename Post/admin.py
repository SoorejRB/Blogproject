from django.contrib import admin

# Register your models here.
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display=("Title", "Author")
    search_fields=["contents"]

class CategoryAdmin(admin.ModelAdmin):
    list_display=("Category_name","Description")

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

