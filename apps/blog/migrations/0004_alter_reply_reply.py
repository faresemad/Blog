# Generated by Django 5.0.1 on 2024-01-09 11:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
