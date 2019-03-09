# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_builder', '0002_add_site_to_callout'),
        ('mp_widgets', '0028_mspwebinarevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstateVerticalLayout',
            fields=[
                ('maincontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='page_builder.MainContent')),
            ],
            options={
                'verbose_name': 'real estate vertical page',
                'verbose_name_plural': 'real estate vertical page',
            },
            bases=('page_builder.maincontent',),
        ),
    ]
