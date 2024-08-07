from django.contrib import admin
from .models import UserModel


class UserSearch(admin.ModelAdmin):
    search_fields = ['fullname', 'username', 'email']


admin.site.register(UserModel, UserSearch, list_display=['fullname', 'username', 'email', 'user_image', 'password'])
