# Generated by Django 4.1.7 on 2023-02-14 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_food_description_food_calories_food_carbs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='Fibers',
            new_name='Fiber',
        ),
    ]
