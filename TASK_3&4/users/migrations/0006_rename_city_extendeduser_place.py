# Generated by Django 3.2.6 on 2021-09-12 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_extendeduser_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduser',
            old_name='city',
            new_name='place',
        ),
    ]
