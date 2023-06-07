# Generated by Django 4.0.3 on 2022-04-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_content', '0004_rename_images_image_rename_videos_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='subTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_theme', models.CharField(max_length=200)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_content.theme')),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='sub_theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_content.subtheme'),
        ),
    ]