# Generated by Django 3.0.1 on 2020-01-07 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_studentattend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentattend',
            old_name='hours1status',
            new_name='hour1status',
        ),
        migrations.RenameField(
            model_name='studentattend',
            old_name='hours2status',
            new_name='hour2status',
        ),
        migrations.RenameField(
            model_name='studentattend',
            old_name='hours3status',
            new_name='hour3status',
        ),
        migrations.RenameField(
            model_name='studentattend',
            old_name='hours4status',
            new_name='hour4status',
        ),
    ]
