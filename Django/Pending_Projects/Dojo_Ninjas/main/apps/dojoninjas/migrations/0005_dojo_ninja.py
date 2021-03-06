# Generated by Django 2.0.5 on 2018-05-16 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dojoninjas', '0004_auto_20180516_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dojo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('Dojos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ninjas', to='dojoninjas.Dojo')),
            ],
        ),
    ]
