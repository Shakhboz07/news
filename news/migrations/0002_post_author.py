# Generated by Django 4.0.5 on 2022-08-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='alex', max_length=150),
            preserve_default=False,
        ),
    ]
