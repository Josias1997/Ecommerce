# Generated by Django 2.2.4 on 2019-09-11 10:46

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('freshniso', '0011_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='countries',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(default='Morocco', max_length=2),
            preserve_default=False,
        ),
    ]
