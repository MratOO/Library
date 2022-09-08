# Generated by Django 4.0.6 on 2022-08-29 12:18

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0039_remove_author_surname_book_read_alter_author_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('book', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='magazine.book', verbose_name='книга')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.ratingstar', verbose_name='звезда')),
            ],
        ),
    ]
