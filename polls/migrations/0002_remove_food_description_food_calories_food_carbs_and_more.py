# Generated by Django 4.1.7 on 2023-02-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='description',
        ),
        migrations.AddField(
            model_name='food',
            name='Calories',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='Carbs',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='Fat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='Fibers',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='Protein',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='Salt',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='Sugar',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
