# Generated by Django 4.0 on 2021-12-17 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_account', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_name', models.CharField(max_length=20)),
                ('msg_email', models.EmailField(max_length=254)),
                ('msg_score', models.IntegerField()),
                ('msg_memo', models.CharField(max_length=200)),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bonus.user')),
            ],
        ),
    ]