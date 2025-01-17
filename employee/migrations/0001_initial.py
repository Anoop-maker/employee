# Generated by Django 5.1.1 on 2024-09-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('idnumber', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]
