from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import UserModel
import os


@receiver(post_delete, sender=UserModel)
def delete_stadion_photo(sender, instance, **kwargs):
    if instance.user_image:
        if os.path.isfile(instance.user_image.path):
            os.remove(instance.user_image.path)
