# Generated by Django 3.2.9 on 2022-12-26 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221223_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.person')),
                ('employment', models.CharField(max_length=50, verbose_name='Empleo')),
            ],
            bases=('home.person',),
        ),
    ]
