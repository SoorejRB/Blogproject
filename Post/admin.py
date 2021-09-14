from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=("Title", "Author")
    search_fields=["contents"]

admin.site.register(Post, PostAdmin)

