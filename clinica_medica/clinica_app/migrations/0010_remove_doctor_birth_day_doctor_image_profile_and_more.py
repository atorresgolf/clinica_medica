# Generated by Django 4.2 on 2023-05-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0009_rename_doctor_id_doctor_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='birth_day',
        ),
        migrations.AddField(
            model_name='doctor',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to='assets/img/doctor_images/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mr_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número de Matrícula'),
        ),
    ]
