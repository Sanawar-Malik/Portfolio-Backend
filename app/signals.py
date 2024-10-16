from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from app.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_define(sender, instance, created, **kwargs):
    if created:
        print('A new user was created', instance.first_name, instance.email)

        
@receiver(pre_save, sender=User)
def user_define(sender, instance, created, **kwargs):
    if created:
        print('A user is about to create save', instance.first_name, instance.email)

@receiver(post_delete, sender=User)
def user_post_delete(sender, instance, **kwargs):
    print('A user has been deleted', instance.first_name, instance.email)

@receiver(pre_delete, sender=User)
def user_delete(sender, instance, **kwargs):
    print('A user is about to be deleted', instance.first_name, instance.email)

