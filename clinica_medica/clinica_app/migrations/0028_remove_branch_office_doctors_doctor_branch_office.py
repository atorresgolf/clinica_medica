# Generated by Django 4.2.1 on 2023-06-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0027_branch_office_delete_branch_offices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch_office',
            name='doctors',
        ),
        migrations.AddField(
            model_name='doctor',
            name='branch_office',
            field=models.ManyToManyField(to='clinica_app.branch_office'),
        ),
    ]
