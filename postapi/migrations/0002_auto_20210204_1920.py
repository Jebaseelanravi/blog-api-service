# Generated by Django 3.1.6 on 2021-02-04 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish_data',
            new_name='publish_date',
        ),
    ]
