from django.db import models


class UserModel(models.Model):
    fullname = models.CharField(max_length=36)
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=36, unique=True)
    password = models.CharField(max_length=36)
    user_image = models.ImageField(upload_to='users_images/', default='users_images/default.jpg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.username)
