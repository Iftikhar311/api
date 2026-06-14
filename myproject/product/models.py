from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    fcm_token = models.CharField(max_length=255, null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )

class ProductSearchHistory(models.Model):
    query         = models.CharField(max_length=255)
    results_count = models.IntegerField(default=0)
    searched_at   = models.DateTimeField(auto_now_add=True)
    user_id       = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.query