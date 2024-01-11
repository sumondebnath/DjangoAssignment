# Generated by Django 4.2.8 on 2024-01-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_Name', models.CharField(max_length=100)),
                ('task', models.ManyToManyField(to='task.task')),
            ],
        ),
    ]