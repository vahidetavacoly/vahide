# Generated by Django 5.1.2 on 2024-11-12 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_padcast_tarikhenteshar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='padcast',
            old_name='file',
            new_name='audio',
        ),
    ]
