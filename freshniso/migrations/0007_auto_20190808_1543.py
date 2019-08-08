# Generated by Django 2.2.4 on 2019-08-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshniso', '0006_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
