# Generated by Django 5.1.6 on 2025-03-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_created_at_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='image'),
        ),
    ]
