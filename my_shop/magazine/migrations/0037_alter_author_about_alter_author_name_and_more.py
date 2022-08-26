# Generated by Django 4.0.6 on 2022-08-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0036_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True, max_length=750),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='author',
            name='years',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]