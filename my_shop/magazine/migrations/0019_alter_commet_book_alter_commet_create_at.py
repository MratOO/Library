# Generated by Django 4.0.6 on 2022-08-25 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0018_remove_commet_parent_commet_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commet',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='magazine.book'),
        ),
        migrations.AlterField(
            model_name='commet',
            name='create_at',
            field=models.DateTimeField(default=-10800),
        ),
    ]
