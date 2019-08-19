# Generated by Django 2.1.7 on 2019-08-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo_main', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('video', models.URLField(blank=True, max_length=255, null=True)),
                ('is_added', models.BooleanField(default=False)),
            ],
        ),
    ]
