# Generated by Django 5.2 on 2025-04-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Student_contact', models.IntegerField()),
                ('Student_age', models.IntegerField()),
                ('Student_plan', models.IntegerField(max_length=40)),
                ('Student_Gender', models.CharField(max_length=50)),
                ('Student_Password', models.CharField(max_length=50)),
                ('Student_message', models.CharField(max_length=211)),
            ],
        ),
    ]
