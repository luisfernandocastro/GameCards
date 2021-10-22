# Generated by Django 3.2.8 on 2021-10-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_rename_nombrejugador_jugadores_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='cartas')),
            ],
            options={
                'verbose_name_plural': 'Cartas',
            },
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categoria'},
        ),
        migrations.AlterModelOptions(
            name='error',
            options={'verbose_name_plural': 'Error'},
        ),
        migrations.AlterModelOptions(
            name='jugadores',
            options={'verbose_name_plural': 'Jugadores'},
        ),
        migrations.AlterModelOptions(
            name='modulo',
            options={'verbose_name_plural': 'Modulo'},
        ),
        migrations.AlterModelOptions(
            name='programador',
            options={'verbose_name_plural': 'Programador'},
        ),
        migrations.AlterField(
            model_name='error',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='errores'),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='modulos'),
        ),
        migrations.AlterField(
            model_name='programador',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='programadores'),
        ),
    ]
