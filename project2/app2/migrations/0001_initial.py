# Generated by Django 5.0.4 on 2024-04-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Emp_Id', models.IntegerField()),
                ('Designation', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
    ]
