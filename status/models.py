from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

# Signal to insert data after migrations
@receiver(post_migrate)
def insert_default_status(sender, **kwargs):
    if sender.name == "status":  # Ensure this runs only for the 'status' app
        Status.objects.get_or_create(
            name="Default Name",
            description="Default Description",
            color="purple",
        )
