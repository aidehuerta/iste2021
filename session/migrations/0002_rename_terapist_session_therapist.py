# Generated by Django 3.2.3 on 2021-06-02 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='terapist',
            new_name='therapist',
        ),
    ]
