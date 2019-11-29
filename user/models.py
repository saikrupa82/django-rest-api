from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    is_admin = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'roles'
