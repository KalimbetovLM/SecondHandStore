# Generated by Django 5.0.1 on 2024-01-11 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category_alter_product_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
