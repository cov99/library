# Generated by Django 3.2.9 on 2022-12-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('age', 'appellative')},
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 18)), name='age_older_18'),
        ),
    ]
