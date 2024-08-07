from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import UserModel
import os


@receiver(post_delete, sender=UserModel)
def delete_user_image(sender, instance, **kwargs):
    if instance.user_image and instance.user_image.name != 'users_images/default.jpg':
        image_path = instance.user_image.path
        if os.path.isfile(image_path):
            try:
                os.remove(image_path)
            except OSError as e:
                print(f'Error: {e.strerror}')
