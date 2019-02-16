# Generated by Django 2.1.1 on 2019-02-16 08:02

import ckeditor_uploader.fields
import colorfield.fields
from django.db import migrations, models
import introduction.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=introduction.models.upload_image_path, verbose_name='Ảnh')),
                ('text_1', models.CharField(blank=True, max_length=500)),
                ('color_1', colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18)),
                ('text_2', models.CharField(blank=True, max_length=500)),
                ('color_2', colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18)),
                ('text_3', models.CharField(blank=True, max_length=500)),
                ('color_3', colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18)),
                ('text_4', models.CharField(blank=True, max_length=500)),
                ('color_4', colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Tên')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Nội dung')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
