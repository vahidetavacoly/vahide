# Generated by Django 5.1.2 on 2025-01-04 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_alter_information_m_user'),
        ('rezerv', '0003_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('appointment_type', models.CharField(choices=[('online', 'آنلاین'), ('offline', 'حضوری')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'در انتظار شروع'), ('in_progress', 'در حال برگزاری'), ('completed', 'پایان یافته'), ('cancelled', 'لغو شده')], default='pending', max_length=20)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='app.information_m')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
