# Generated by Django 3.0.4 on 2020-03-19 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200318_0043'),
    ]

    operations = [
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
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stories.School'),
            preserve_default=False,
        ),
    ]
