# Generated by Django 5.1.6 on 2025-02-12 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('IN_STOCK', '在库'), ('ALLOCATED', '已领用'), ('MAINTENANCE', '维修'), ('SCRAPPED', '已报废')], default='IN_STOCK', max_length=20, verbose_name='资产状态'),
        ),
        migrations.AddField(
            model_name='asset',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.assetcategory', verbose_name='资产类别'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.assettype', verbose_name='资产类型'),
        ),
    ]
