# Generated by Django 5.1.6 on 2025-02-12 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_assetcategory_assettype_alter_asset_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='asset_id',
            new_name='asset_code',
        ),
    ]
