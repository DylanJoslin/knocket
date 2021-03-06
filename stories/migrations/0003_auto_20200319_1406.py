# Generated by Django 3.0.4 on 2020-03-19 20:06

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_videopost_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'school',
                'verbose_name_plural': 'schools',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='videopost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='videopost',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videopost',
            name='video',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AddField(
            model_name='videopost',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stories.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videopost',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.School'),
        ),
    ]
