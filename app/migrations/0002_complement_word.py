# Generated by Django 3.2.7 on 2021-09-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='word searched', max_length=50)),
                ('meaning', models.CharField(help_text='word meaning', max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Complement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='word searched', max_length=50)),
                ('meaning', models.CharField(help_text='word meaning', max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ManyToManyField(to='app.Word')),
            ],
        ),
    ]
