# Generated by Django 4.2.7 on 2023-12-19 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0005_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='full_name',
            new_name='voter_ID',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='candidate_choice',
        ),
    ]
