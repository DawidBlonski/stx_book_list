# Generated by Django 3.1.2 on 2020-10-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0002_remove_book_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(null=True),
        ),
    ]
