# Generated by Django 5.0.6 on 2024-06-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(db_default=True, default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='order',
            name='suborders',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8),
        ),
    ]