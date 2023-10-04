from django.db.models.signals import pre_save
from django.dispatch import receiver
from . models import Leader

@receiver(pre_save, sender=Leader)
def set_default_image(sender, instance, **kwargs):
    if not instance.image:
        instance.image = 'default.jpg'