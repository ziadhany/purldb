# Generated by Django 4.1.2 on 2022-11-17 23:41

# Generated by Django 4.1.2 on 2022-11-17 18:43

from django.db import migrations


def replace_http_with_https_in_maven_uris(apps, _):
    ResourceURI = apps.get_model("minecode", "ResourceURI")
    resource_uris = ResourceURI.objects.filter(
        uri__startswith="http://repo1.maven.org",
    ).iterator(chunk_size=5000)
    updated = []
    for i, resource_uri in enumerate(resource_uris):
        if not i % 5000:
            ResourceURI.objects.bulk_update(
                objs=updated,
                fields=[
                    "uri",
                ]
            )
            updated = []
        uri = resource_uri.uri
        _, uri_remains = uri.split("http://repo1.maven.org")
        new_uri = "https://repo1.maven.org" + uri_remains
        resource_uri.uri = new_uri
        updated.append(resource_uri)
    if updated:
        ResourceURI.objects.bulk_update(
            objs=updated,
            fields=[
                "uri",
            ]
        )


class Migration(migrations.Migration):

    dependencies = [
        ("minecode", "0026_set_is_visitable_for_maven_index_uris"),
    ]

    operations = [
        migrations.RunPython(replace_http_with_https_in_maven_uris, migrations.RunPython.noop),
    ]