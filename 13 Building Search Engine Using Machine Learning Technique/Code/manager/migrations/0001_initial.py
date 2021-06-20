# Generated by Django 3.0.5 on 2020-07-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='managerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('passwd', models.CharField(max_length=40)),
                ('cwpasswd', models.CharField(max_length=40)),
                ('mobileno', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'managerregister',
            },
        ),
    ]
