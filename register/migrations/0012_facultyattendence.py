# Generated by Django 3.0.1 on 2020-01-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_studentmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='facultyattendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=5)),
                ('factid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('hours1status', models.CharField(max_length=5)),
                ('hours2status', models.CharField(max_length=5)),
                ('hours3status', models.CharField(max_length=5)),
                ('hours4status', models.CharField(max_length=5)),
            ],
        ),
    ]
