from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status')
    search_fields=('title','body')
    raw_id_fields = ('author',)
    ordering = ['status','publish']


admin.site.register(Post,PostAdmin)