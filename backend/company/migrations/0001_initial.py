# Generated by Django 2.2.2 on 2019-06-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('web_site', models.CharField(max_length=100)),
                ('logo_path', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]