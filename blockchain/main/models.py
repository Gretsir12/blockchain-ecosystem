from django.db import models

# Create your models here.

class User(AbstractUser)):

    def __str__(self):
        return self.username
