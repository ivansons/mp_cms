from django import forms
from django.utils.translation import ugettext_lazy as _

from widgy.models.links import LinkFormField, LinkFormMixin


class CallToActionForm(LinkFormMixin, forms.ModelForm):
    link = LinkFormField(label=_('Link'), required=False)


css_style_form_field = forms.CharField(
    label=_('CSS style'), required=False,
    widget=forms.TextInput)


text_form_field = forms.CharField(
    label=_('Main text'), required=False,
    max_length=1000, widget=forms.Textarea)


def modelform_factory(name, **kwargs):
    return type(name, (forms.ModelForm,), kwargs)
