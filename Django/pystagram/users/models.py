from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_image=models.ImageField(
        "프로필이미지",upload_to="users/profile",blank=True)
    short_description = models.TextField("소개글",blank=True)
    like_posts=models.ManyToManyField(
        "posts.POST",
        verbose_name="좋아요 누른 Post 목록",
        related_name="Like_users",
        blank=True,
    )
    def __str__(self):
        return self.username
    