# -*- coding: utf8 -*-
"""
Matterport-specific common app forms
"""
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

from haystack.forms import ModelSearchForm as _ModelSearchForm, model_choices

from .validators import validate_http_status_code, validate_country_code


class FreeGeoIPLogForm(forms.Form):
    freegeoip_status = forms.CharField(label='Freegeoip Status', max_length=3,
                                       validators=[validate_http_status_code])

    freegeoip_country_code = forms.CharField(
        label='Freegeoip Country Code',
        max_length=2,
        validators=[validate_country_code])


class ModelSearchForm(_ModelSearchForm):
    """
    Customized `ModelSearchForm` to better represent models
    """

    extra_model_choices = {
        'blog': ('zinnia.entry', ('blog', 'Blog entries')),
        'gallery': ('mp_blog.modelentry', ('gallery', 'Model entries')),
        'news': ('mp_blog.newsentry', ('news', 'News entries')),
        'resource': ('mp_blog.resourceentry',
                     ('resource', 'Resource entries')),
        'casestudy': ('mp_blog.casestudyentry',
                      ('case study', 'Case study entries')),
        'region': ('mp_blog.regionentry', ('region', 'Region entries')),
    }

    def __init__(self, *args, **kwargs):
        super(_ModelSearchForm, self).__init__(*args, **kwargs)
        extra_choices = [v[1] for v in self.extra_model_choices.values()]
        self.fields['resource'] = forms.MultipleChoiceField(
            choices=model_choices() + extra_choices,
            required=False,
            label=_('Search In'),
            widget=forms.CheckboxSelectMultiple)

    def get_models(self):
        """Return an alphabetical list of model classes in the index."""
        search_models = []

        if self.is_valid():
            for model in self.cleaned_data['resource']:
                if model in self.extra_model_choices:
                    model = self.extra_model_choices[model][0]
                search_models.append(models.get_model(*model.split('.')))

        return search_models
