# Generated by Django 3.1.5 on 2021-04-02 17:58

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0047_add_search_vector_field_to_package'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='package',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='packagedb_p_search__8d33bb_gin'),
        ),
    ]