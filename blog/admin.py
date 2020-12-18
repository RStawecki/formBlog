from django.contrib import admin
from blog.models import Post

class DisplayDate(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Post, DisplayDate)

