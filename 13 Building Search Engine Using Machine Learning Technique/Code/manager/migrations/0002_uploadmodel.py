# Generated by Django 3.0.5 on 2020-07-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('filetype', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
        ),
    ]