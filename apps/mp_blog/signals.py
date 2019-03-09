from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver

from ckeditor_uploader import image_processing
from ckeditor_uploader.views import ImageUploadView

from zinnia.models.entry import Entry


@receiver(post_save, sender=Entry, dispatch_uid='create_thumbnail')
def create_thumbnail_callback(sender, instance, **kwargs):
    """
    Creates a thumbnail if it hasn't been created already by CKEditor or
    Django Filer
    """
    illustration_image = getattr(instance, 'image', None)
    if illustration_image:
        backend = image_processing.get_backend()
        ImageUploadView._create_thumbnail_if_needed(backend,
                                                    illustration_image.name)
