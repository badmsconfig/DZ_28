# Generated by Django 5.0.1 on 2024-03-12 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.TextField(blank=True)),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('coreobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogapp.coreobject')),
                ('description', models.TextField()),
            ],
            bases=('blogapp.coreobject',),
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('coreobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogapp.coreobject')),
                ('text', models.TextField()),
            ],
            bases=('blogapp.coreobject',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.TextField(blank=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
                ('tags', models.ManyToManyField(to='blogapp.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Imajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(to='blogapp.tag')),
            ],
        ),
    ]
