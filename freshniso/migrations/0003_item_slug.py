# Generated by Django 2.2.4 on 2019-08-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshniso', '0002_auto_20190808_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
