# Generated by Django 4.1.5 on 2023-01-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_alter_movie_age_restriction_remove_movie_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='released',
            field=models.IntegerField(),
        ),
    ]