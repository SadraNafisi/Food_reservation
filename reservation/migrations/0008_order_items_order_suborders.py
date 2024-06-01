# Generated by Django 5.0.6 on 2024-05-31 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_rename_is_confirm_order_is_confirmed'),
    ]

    operations = [
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
    ]