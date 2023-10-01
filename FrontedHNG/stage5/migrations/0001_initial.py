# Generated by Django 4.2.5 on 2023-10-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('transcript', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
