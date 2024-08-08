import os
from django.db import models
from django.core.exceptions import ValidationError
from apps.user.models import UserModel


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are {valid_extensions}')


class PostModel(models.Model):
    post_file = models.FileField(upload_to='post_files/', validators=[validate_file_extension])
    post_title = models.CharField(max_length=100, null=True)
    post_likes = models.ManyToManyField(UserModel, related_name='liked_posts', blank=True)
    post_author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    post_created = models.DateTimeField(auto_now_add=True)
