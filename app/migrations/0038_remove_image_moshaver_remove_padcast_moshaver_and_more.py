# Generated by Django 5.1.1 on 2024-12-04 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_message_user_alter_message_ferstande_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='moshaver',
        ),
        migrations.RemoveField(
            model_name='padcast',
            name='moshaver',
        ),
        migrations.RemoveField(
            model_name='test',
            name='moshaver',
        ),
        migrations.RemoveField(
            model_name='vidio',
            name='moshaver',
        ),
        migrations.AddField(
            model_name='information_m',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.image'),
        ),
        migrations.AddField(
            model_name='information_m',
            name='padcast',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.padcast'),
        ),
        migrations.AddField(
            model_name='information_m',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.test'),
        ),
        migrations.AddField(
            model_name='information_m',
            name='vidio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vidio'),
        ),
    ]