# Generated by Django 5.0.1 on 2024-02-08 15:20

import django.db.models.deletion
import magazin.utilities
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.CharField(default=magazin.utilities.set_id, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('accepter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepter', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
