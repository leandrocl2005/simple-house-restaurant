# Generated by Django 3.2 on 2021-04-30 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='preço')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food', to='food.category')),
            ],
            options={
                'verbose_name': 'Comida',
                'verbose_name_plural': 'Comidas',
                'ordering': ('name',),
            },
        ),
    ]