# Generated by Django 5.1.3 on 2024-12-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='recipes/'),
        ),
    ]
