# Generated by Django 3.1.7 on 2021-04-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210419_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d', verbose_name='аватар'),
        ),
    ]