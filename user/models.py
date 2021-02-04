from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

import uuid

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=100)
    unique_address = models.CharField(unique=True, max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        unique_code = uuid.uuid4()
        self.unique_address = slugify(self.address) +'-'+str(unique_code)[:8]
        super(User, self).save(*args, **kwargs)

