# Generated by Django 4.1.5 on 2023-02-06 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_alter_staff_awards'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
    ]