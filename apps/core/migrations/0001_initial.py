# Generated by Django 3.1.4 on 2021-01-21 21:40

import apps.core.managers.user
import apps.core.models.api_key
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
                'default_permissions': ('add', 'delete'),
            },
            managers=[
                ('objects', apps.core.managers.user.UserManager()),
                ('all_objects', apps.core.managers.user.UserManager(alive_only=False)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('url_name', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='catalogs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
                'db_table': 'catalogs',
                'default_permissions': (),
                'unique_together': {('creator_id', 'title')},
            },
        ),
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('platform', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('web', 'web'), ('debug', 'debug'), ('custom', 'custom'), ('user', 'user')], default=apps.core.models.api_key.ApiKey.DevicePlatform['WEB'], enum_class=apps.core.models.api_key.ApiKey.DevicePlatform, max_length=6)),
                ('secret', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'API key',
                'verbose_name_plural': 'API keys',
                'db_table': 'api_keys',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('url_name', models.SlugField()),
                ('content', models.TextField()),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='core.catalog')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
                'db_table': 'feeds',
                'default_permissions': (),
                'unique_together': {('creator_id', 'url_name'), ('creator_id', 'title')},
            },
        ),
    ]
