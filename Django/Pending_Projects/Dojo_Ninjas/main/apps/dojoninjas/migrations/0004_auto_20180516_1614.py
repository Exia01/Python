# Generated by Django 2.0.5 on 2018-05-16 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninjas', '0003_dojo_ninja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='Dojos',
        ),
        migrations.DeleteModel(
            name='Dojo',
        ),
        migrations.DeleteModel(
            name='Ninja',
        ),
    ]
