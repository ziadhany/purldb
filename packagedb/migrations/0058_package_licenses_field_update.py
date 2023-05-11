# Generated by Django 4.1.2 on 2023-05-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0057_alter_package_version"),
    ]

    operations = [
        migrations.RenameField(
            model_name="package",
            old_name="license_expression",
            new_name="declared_license_expression",
        ),
        migrations.AlterField(
            model_name="package",
            name="declared_license_expression",
            field=models.TextField(
                blank=True,
                null=True,
                help_text="The license expression for this package typically derived from its extracted_license_statement or from some other type-specific routine or convention.",
            ),
        ),
       migrations.RenameField(
            model_name="package",
            old_name="declared_license",
            new_name="extracted_license_statement",
        ),
        migrations.AlterField(
            model_name="package",
            name="extracted_license_statement",
            field=models.TextField(
                blank=True,
                null=True,
                help_text="The license statement mention, tag or text as found in a package manifest and extracted. This can be a string, a list or dict of strings possibly nested, as found originally in the manifest.",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="declared_license_expression_spdx",
            field=models.TextField(
                blank=True,
                null=True,
                help_text="The SPDX license expression for this package converted from its declared_license_expression.",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="holder",
            field=models.TextField(
                blank=True,
                null=True,
                help_text="Holders for this package. Typically one per line.",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="license_detections",
            field=models.JSONField(
                blank=True,
                null=True,
                default=list,
                help_text="A list of LicenseDetection mappings typically derived from its extracted_license_statement or from some other type-specific routine or convention.",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="other_license_detections",
            field=models.JSONField(
                blank=True,
                null=True,
                default=list,
                help_text="A list of LicenseDetection mappings which is different from the declared_license_expression, (i.e. not the primary license) These are detections for the detection for the license expressions in other_license_expression. ",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="other_license_expression",
            field=models.TextField(
                blank=True,
                null=True,
                help_text="The license expression for this package which is different from the declared_license_expression, (i.e. not the primary license) routine or convention.",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="other_license_expression_spdx",
            field=models.TextField(
                blank=True,
                null=True,
                help_text="The other SPDX license expression for this package converted from its other_license_expression.",
            ),
        ),
    ]
