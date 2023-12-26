# Generated by Django 5.0 on 2023-12-26 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beyblade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('faceBolt', models.CharField(blank=True, max_length=100, null=True)),
                ('fusionWheel', models.CharField(blank=True, choices=[('Storm', 'Storm'), ('Dark', 'Dark'), ('Rock', 'Rock'), ('Flame', 'Flame'), ('Lightning', 'Lightning'), ('Earth', 'Earth'), ('Killer', 'Killer'), ('Thermal', 'Thermal'), ('Burn', 'Burn'), ('Poison', 'Poison'), ('Galaxy', 'Galaxy'), ('Gravity', 'Gravity'), ('Cyclone', 'Cyclone'), ('Cyber', 'Cyber'), ('Hell', 'Hell'), ('Bassalt', 'Bassalt')], max_length=100, null=True)),
                ('spinDirection', models.CharField(blank=True, choices=[('Clockwise', 'Clockwise'), ('Counter-clockwise', 'Counter-clockwise'), ('Variable', 'Variable')], max_length=100, null=True)),
                ('weightGrams', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('abilities', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CurAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('houseNo', models.IntegerField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('province', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstName', models.CharField(blank=True, max_length=50, null=True)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('homeTown', models.CharField(blank=True, max_length=250, null=True)),
                ('homeCountry', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('curAddr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_mentor', to='beyblademasterapp.curaddress')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstName', models.CharField(blank=True, max_length=50, null=True)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('homeTown', models.CharField(blank=True, max_length=250, null=True)),
                ('homeCountry', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('curAddr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_player', to='beyblademasterapp.curaddress')),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beyblademasterapp.curaddress')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('acquisition_date', models.DateField()),
                ('beyblade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beyblademasterapp.beyblade')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beyblademasterapp.player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
