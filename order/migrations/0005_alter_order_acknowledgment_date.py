# Generated by Django 4.2.7 on 2023-12-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_expeted_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
