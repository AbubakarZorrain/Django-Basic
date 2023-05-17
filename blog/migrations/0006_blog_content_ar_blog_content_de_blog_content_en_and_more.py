# Generated by Django 4.2.1 on 2023-05-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_it',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_ja',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_ko',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_pt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_ur',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_zh_hans',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_it',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_zh_hans',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
