# Generated by Django 3.0.1 on 2020-01-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20200107_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='factleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fromdate', models.DateField(max_length=5)),
                ('todate', models.DateField(max_length=5)),
                ('reason', models.CharField(max_length=5)),
            ],
        ),
    ]
