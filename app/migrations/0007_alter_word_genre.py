# Generated by Django 3.2.7 on 2021-10-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210925_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='genre',
            field=models.ManyToManyField(blank=True, help_text='choice one or more categories', null=True, to='app.Genre'),
        ),
    ]
