# Generated by Django 3.2.7 on 2021-09-22 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210921_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]
