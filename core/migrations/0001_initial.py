# Generated by Django 4.1.7 on 2023-03-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
