# Generated by Django 4.0.6 on 2022-08-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0007_rename_title_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=None, max_length=75),
        ),
    ]