# myapp/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .utils.groups_setup import setup_groups_and_permissions


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == "myapp":  # limit to your app
        setup_groups_and_permissions()
