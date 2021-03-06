# Generated by Django 4.0.4 on 2022-06-10 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livetapes_api', '0003_remove_show_tracks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_notes', to='livetapes_api.show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
