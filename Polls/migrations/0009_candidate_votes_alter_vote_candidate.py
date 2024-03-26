# Generated by Django 4.2.7 on 2024-01-04 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0008_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vote',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_received', to='Polls.candidate'),
        ),
    ]
