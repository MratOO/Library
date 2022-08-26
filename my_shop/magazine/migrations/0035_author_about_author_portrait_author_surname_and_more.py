# Generated by Django 4.0.6 on 2022-08-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0034_remove_book_price_alter_book_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='portrait',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='author',
            name='surname',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AddField(
            model_name='author',
            name='years',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
