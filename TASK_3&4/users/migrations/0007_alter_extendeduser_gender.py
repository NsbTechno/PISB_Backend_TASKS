# Generated by Django 3.2.6 on 2021-09-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_city_extendeduser_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=' ', max_length=12, null=True),
        ),
    ]
