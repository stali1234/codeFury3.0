# Generated by Django 3.1.3 on 2020-11-07 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('slug', models.SlugField()),
                ('adhar', models.CharField(max_length=12, unique=True)),
                ('dateTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('dob', models.DateField()),
                ('work', models.CharField(choices=[('carpenter', 'carpenter'), ('handloom worker', 'handloom worker'), ('labour', 'labour'), ('Other', 'Other')], default=None, max_length=100)),
                ('other', models.CharField(blank=True, max_length=100)),
                ('is_employed', models.BooleanField(blank=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('slug', models.SlugField()),
                ('CBDT_id', models.IntegerField(unique=True)),
                ('adhar', models.CharField(max_length=12, unique=True)),
                ('dateTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('dob', models.DateField()),
                ('work', models.CharField(choices=[('carpenter', 'carpenter'), ('handloom worker', 'handloom worker'), ('labour', 'labour'), ('Other', 'Other')], default=None, max_length=100)),
                ('other', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField(default=None)),
                ('Ammount_paid', models.IntegerField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
