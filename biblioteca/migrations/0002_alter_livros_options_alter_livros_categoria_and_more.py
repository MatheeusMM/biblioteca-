# Generated by Django 4.0.5 on 2022-06-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name_plural': 'Livro'},
        ),
        migrations.AlterField(
            model_name='livros',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='livros',
            name='editora',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Editora',
        ),
    ]
