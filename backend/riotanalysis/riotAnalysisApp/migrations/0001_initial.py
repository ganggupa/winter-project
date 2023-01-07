# Generated by Django 4.1.4 on 2023-01-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Augment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('augment_apiName', models.CharField(blank=True, max_length=200, null=True)),
                ('augment_info', models.CharField(blank=True, max_length=200, null=True)),
                ('augment_img', models.ImageField(blank=True, default='', upload_to='gameimages/')),
                ('augment_id', models.IntegerField()),
                ('augment_name', models.CharField(blank=True, max_length=200, null=True)),
                ('augment_effect', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('item_img', models.ImageField(blank=True, default='', upload_to='gameimages/')),
                ('item_info', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('item_apiName', models.CharField(blank=True, max_length=200, null=True)),
                ('item_effect', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='MatchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, max_length=100)),
                ('puuid', models.CharField(blank=True, max_length=1000)),
                ('game_type', models.CharField(blank=True, max_length=1000)),
                ('set_number', models.IntegerField(default=0)),
                ('last_level', models.IntegerField()),
                ('placement', models.IntegerField()),
                ('last_round', models.IntegerField()),
                ('play_time', models.FloatField()),
                ('gold_left', models.IntegerField()),
                ('total_damage_to_players', models.IntegerField()),
                ('augments1', models.CharField(blank=True, max_length=100)),
                ('augments2', models.CharField(blank=True, max_length=100)),
                ('augments3', models.CharField(blank=True, max_length=100)),
                ('traits', models.JSONField()),
                ('units', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_name', models.CharField(blank=True, max_length=200, null=True)),
                ('trait_apiName', models.CharField(blank=True, max_length=200, null=True)),
                ('trait_img', models.ImageField(blank=True, default='', upload_to='gameimages/')),
                ('trait_effect', models.JSONField()),
                ('trait_info', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpperItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('item_img', models.ImageField(blank=True, default='', upload_to='gameimages/')),
                ('item_info', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('item_apiName', models.CharField(blank=True, max_length=200, null=True)),
                ('item_effect', models.JSONField()),
                ('base_items', models.ManyToManyField(related_name='base_item', to='riotanalysisapp.baseitem')),
            ],
        ),
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_apiName', models.CharField(blank=True, max_length=300, null=True)),
                ('champion_variables', models.JSONField()),
                ('champion_name', models.CharField(blank=True, max_length=200, null=True)),
                ('champion_img', models.ImageField(blank=True, default='', upload_to='gameimages/')),
                ('champion_info', models.CharField(blank=True, max_length=1000, null=True)),
                ('champion_stats', models.JSONField()),
                ('champion_cost', models.IntegerField()),
                ('traits', models.ManyToManyField(related_name='trait', to='riotanalysisapp.trait')),
            ],
        ),
    ]
