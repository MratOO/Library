# Generated by Django 4.0.6 on 2022-08-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0038_alter_author_portrait'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='surname',
        ),
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='portrait',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
