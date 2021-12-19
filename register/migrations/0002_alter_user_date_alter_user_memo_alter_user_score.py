# Generated by Django 4.0 on 2021-12-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='memo',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.IntegerField(max_length=2),
        ),
    ]
