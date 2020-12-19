from django.db import models
from registration_app.models import *
import re
import bcrypt
from datetime import datetime



class Wall_message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)