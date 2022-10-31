# Generated by Django 3.1.3 on 2020-12-16 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0043_lowercase_purl_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='history',
            field=models.TextField(blank=True, editable=False, help_text='History for this object a text where each line has the form: "<timestamp><one space><message>". Append-only and not editable.'),
        ),
    ]