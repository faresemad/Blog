# Generated by Django 5.0.1 on 2024-01-07 11:22

import ckeditor.fields
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models
import apps.utils.custome_models


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique_for_date='publish')),
                ('body', ckeditor.fields.RichTextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', apps.utils.custome_models.ListField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-publish',),
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='blog.post')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['slug', 'publish'], name='blog_post_slug_c84a29_idx'),
        ),
    ]
