# Generated by Django 4.2 on 2023-05-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.CharField(default='No description available', max_length=500),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
