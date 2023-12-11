# Generated by Django 4.2.7 on 2023-12-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='acknowledgment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='po_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='quality_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'pending'), ('2', 'completed'), ('3', 'cancelled')], max_length=25),
        ),
    ]