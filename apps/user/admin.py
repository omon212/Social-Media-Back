from django.contrib import admin
from .models import *


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'username', 'email', 'user_image', 'password']
    search_fields = ['fullname', 'username', 'email']


class FollowModelAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user', 'subscriber_count', 'subscription_count']

    def subscriber_count(self, obj):
        return obj.subscribers.count()

    subscriber_count.short_description = 'Subscribers'

    def subscription_count(self, obj):
        return obj.subscriptions.count()

    subscription_count.short_description = 'Subscriptions'


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(FollowModel, FollowModelAdmin)
