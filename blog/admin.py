from django.contrib import admin
from .models import PostModel, Comment

# Register your models here.


# this is to display the title and date_created in the backend at the admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')


admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)
