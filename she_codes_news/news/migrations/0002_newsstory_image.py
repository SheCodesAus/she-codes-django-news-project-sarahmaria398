# Generated by Django 4.0.1 on 2022-06-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
