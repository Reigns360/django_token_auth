# Generated by Django 4.2.7 on 2024-01-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0011_vote_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='photo',
            field=models.ImageField(default='default_photo.jpg', upload_to='photos/'),
        ),
    ]
