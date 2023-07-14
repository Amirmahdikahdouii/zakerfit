from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserPhoneNumberValidation


@receiver(post_save, sender=get_user_model())
def user_post_save_handler(sender, instance, created: bool, **kwargs):
    if created:
        import random
        UserPhoneNumberValidation.objects.create(user=instance, code=random.randint(100000, 999999))
