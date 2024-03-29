# Generated by Django 5.0.1 on 2024-02-04 14:06

import django.db.models.deletion
import magazin.utilities
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_image_delete_productimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('PB', 'Published'), ('BK', 'Blocked')], default='PB', max_length=2),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.CharField(default=magazin.utilities.set_id, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
