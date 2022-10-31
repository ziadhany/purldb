# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-17 11:09
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0004_auto_20160713_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='last_modified_date',
            new_name='origin_date',
        ),
        migrations.AlterField(
            model_name='package',
            name='origin_date',
            field=models.DateField(blank=True, db_index=True, help_text='Timestamp set to the last modified date of the remote Resource, such as the modified date of a file, the lastmod value on a sitemap or the modified date returned by an HTTP resource.', null=True),
        ),
    ]