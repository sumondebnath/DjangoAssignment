# Generated by Django 4.2.8 on 2024-01-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField()),
                ('isCompleted', models.BooleanField(default=False)),
                ('TaskAssignDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]