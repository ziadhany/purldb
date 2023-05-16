# Generated by Django 4.1.2 on 2023-05-16 01:27

from django.db import migrations


def set_package_content_field(apps, schema_editor):
    # TODO: have separate job that updates the package_content field
    Package = apps.get_model("packagedb", "Package")
    packages = Package.objects.filter(
        package_content__isnull=True
    ).iterator(
        chunk_size=5000
    )
    updated = []
    for i, package in enumerate(packages):
        if not i % 5000:
            Package.objects.bulk_update(
                objs=updated,
                fields=[
                    "package_content"
                ]
            )
            updated = []
        if 'source' in package.qualifiers:
            package.package_content = Package.PackageContentType.SOURCE
            updated.append(package)
    if updated:
        Package.objects.bulk_update(
            objs=updated,
            fields=[
                "package_content"
            ]
        )


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0064_package_package_content_package_package_set"),
    ]

    operations = [
        migrations.RunPython(
            set_package_content_field,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
