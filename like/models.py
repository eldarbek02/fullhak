from django.db import models
from post.models import Posts
from django.contrib.auth import get_user_model
from account.models import User


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False,blank=True)


    def __str__(self):
        return f'{self.author}{self.post}'