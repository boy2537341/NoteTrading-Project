# Generated by Django 4.0 on 2022-01-01 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0009_alter_msg_score'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
        migrations.AlterModelOptions(
            name='msg',
            options={'ordering': ['-date', '-person_id']},
        ),
        migrations.RenameField(
            model_name='msg',
            old_name='user_id',
            new_name='person_id',
        ),
    ]
