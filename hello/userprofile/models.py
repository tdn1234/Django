from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    avatar_path = 'static/images/'
    region = models.CharField(max_length=120)
    interests = models.CharField(max_length=120)
    specialism = models.CharField(max_length=120)
    avatar = models.ImageField(
                               'profile picture',
                               upload_to=avatar_path,
                               null=True,
                               blank=True
                               )
    user = models.ForeignKey(User, unique=True)

    def __str__(self):
        return self.user.username

    def get_user_avatar(self):
        if self.avatar:
            return self.avatar
        return 'images/default.jpeg'
