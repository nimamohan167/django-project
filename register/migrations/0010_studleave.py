# Generated by Django 3.0.1 on 2020-01-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_factleave'),
    ]

    operations = [
        migrations.CreateModel(
            name='studleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fromdate', models.DateField(max_length=5)),
                ('todate', models.DateField(max_length=5)),
                ('reason', models.CharField(max_length=5)),
            ],
        ),
    ]
