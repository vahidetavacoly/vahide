# Generated by Django 5.1.2 on 2024-11-17 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_file_padcast_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='information_m',
            name='image1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.image'),
        ),
        migrations.AddField(
            model_name='information_m',
            name='padcast1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.padcast'),
        ),
        migrations.AddField(
            model_name='information_m',
            name='test1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.test'),
        ),
        migrations.AddField(
            model_name='information_m',
            name='vidio1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vidio'),
        ),
        migrations.AlterField(
            model_name='padcast',
            name='audio',
            field=models.FileField(upload_to='files/padcast'),
        ),
    ]
