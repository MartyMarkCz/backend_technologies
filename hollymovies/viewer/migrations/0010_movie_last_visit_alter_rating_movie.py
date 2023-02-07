# Generated by Django 4.1.5 on 2023-02-07 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_alter_genre_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='last_visit',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating', to='viewer.movie'),
        ),
    ]
