# Generated by Django 5.0.6 on 2024-07-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addrestaurant', '0002_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='number_of_people',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
