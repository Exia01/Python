# Generated by Django 2.1.4 on 2019-01-06 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20190103_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
