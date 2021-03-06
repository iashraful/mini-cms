# Generated by Django 2.0.1 on 2018-02-07 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuAccessControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('access_type', models.IntegerField(choices=[(0, 'All'), (3, 'Create'), (2, 'Edit'), (4, 'NoAccess'), (1, 'View')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MenuGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('path', models.CharField(max_length=64, unique=True)),
                ('is_dropdown', models.BooleanField(default=False)),
                ('auth', models.BooleanField(default=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_main_menu', models.BooleanField(default=True)),
                ('dropdown_items', models.ManyToManyField(blank=True, related_name='_menugroup_dropdown_items_+', to='client_config.MenuGroup')),
                ('submenus', models.ManyToManyField(blank=True, related_name='_menugroup_submenus_+', to='client_config.MenuGroup')),
            ],
        ),
        migrations.AddField(
            model_name='menuaccesscontrol',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client_config.MenuGroup'),
        ),
    ]
