# Generated by Django 3.2.6 on 2021-09-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_extendeduser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='email',
            field=models.EmailField(default=-1.0, max_length=254),
            preserve_default=False,
        ),
    ]
