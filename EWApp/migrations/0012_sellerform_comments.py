# Generated by Django 3.2.8 on 2022-01-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EWApp', '0011_remove_sellerform_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerform',
            name='comments',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
