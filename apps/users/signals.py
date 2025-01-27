# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def assign_default_role(sender, instance, created, **kwargs):
    if created and not instance.role:
        instance.role = Role.objects.get_or_create(name="Customer")[0]
        instance.save()