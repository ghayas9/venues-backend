from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def auto_approve_admin(sender, instance, created, **kwargs):
    """
    Automatically approves admin users if certain conditions are met.
    This is an example signal handler triggered after saving a CustomUser.
    """
    if created and instance.role == 'admin':
        # For example, you might auto-approve based on specific criteria
        instance.is_approved = False  # Default behavior: admin approval required
        instance.save()
