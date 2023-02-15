# Generated by Django 3.2.6 on 2021-11-13 02:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0048_add_gin_index_to_search_vector_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='extra_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='An optional JSON-formatted field to identify additional resource attributes.'),
        ),
    ]