# Generated by Django 3.0.7 on 2020-06-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('Task', models.TextField(blank=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
