# Generated by Django 3.2.4 on 2021-07-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210701_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_like',
            field=models.IntegerField(null=True, verbose_name='Beğeni'),
        ),
    ]
