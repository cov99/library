# Generated by Django 3.2.9 on 2022-12-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pseudonym',
            field=models.CharField(blank=True, max_length=50, verbose_name='seudonimo'),
        ),
    ]
