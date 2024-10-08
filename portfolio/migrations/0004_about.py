# Generated by Django 5.1 on 2024-08-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_chocolate'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/about')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
        ),
    ]
