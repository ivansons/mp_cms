import os

from django import forms
from django.db.models import CharField

from filer.models.filemodels import File

from widgy.contrib.page_builder.db.fields import ImageField as BaseImageField

from .validators import validate_hex_color, validate_iframe_tag
from .widgets import ColorPickerWidget


class HexColorField(CharField):
    """
    A custom CharField that stores hex color value (`#000`, `#fafafa`, etc.)
    """
    default_validators = [validate_hex_color]
    widget = ColorPickerWidget

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super(HexColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = self.widget
        return super(HexColorField, self).formfield(**kwargs)


class IframeTagField(CharField):
    """
    A custom CharField for <iframe> tag
    """
    default_validators = [validate_iframe_tag]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 1000
        super(IframeTagField, self).__init__(*args, **kwargs)


class ImageField(BaseImageField):
    """
    A custom ImageField that supports setting accepted files.
    """
    accepted_files = ['.jpg', '.jpeg', '.png', '.gif']

    def __init__(self, *args, **kwargs):
        accepted_files = kwargs.pop('accepted_files', None)
        super(ImageField, self).__init__(*args, **kwargs)
        if accepted_files and isinstance(accepted_files, list):
            self.accepted_files = accepted_files

    def validate(self, value, model_instance):
        file_obj = File.objects.get(pk=value)
        iext = os.path.splitext(file_obj.file.name)[1].lower()
        if iext not in self.accepted_files:
            raise forms.ValidationError(
                'File type must be {}'.format(' '.join(self.accepted_files)))
