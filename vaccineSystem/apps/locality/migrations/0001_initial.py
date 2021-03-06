# Generated by Django 3.2.9 on 2021-11-29 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schools', to='locality.municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Polyclinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='polyclinics', to='locality.municipality')),
            ],
        ),
        migrations.AddField(
            model_name='municipality',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='municipalities', to='locality.province'),
        ),
        migrations.CreateModel(
            name='ConsultingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('polyclinic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consulting_rooms', to='locality.polyclinic')),
            ],
        ),
    ]
