# Generated by Django 3.2 on 2021-04-25 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_sqlcode_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Code',
            new_name='GeneratedCode',
        ),
    ]
