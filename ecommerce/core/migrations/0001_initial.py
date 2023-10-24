# Generated by Django 4.2.4 on 2023-10-24 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=3, verbose_name='Tipo')),
                ('vencimiento', models.DateField(null=True, verbose_name='Fecha vencimiento')),
            ],
        ),
        migrations.CreateModel(
            name='IngresoInsumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de ingreso')),
                ('cerveza', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.cerveza')),
            ],
        ),
        migrations.CreateModel(
            name='Proovedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nobre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('empresa', models.CharField(max_length=50, verbose_name='Empresa')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('cerveza', models.ManyToManyField(through='core.IngresoInsumos', to='core.cerveza')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ingresoinsumos',
            name='proovedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.proovedor'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nobre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('nickname', models.CharField(max_length=50, verbose_name='Nickname')),
                ('password', models.CharField(max_length=45, verbose_name='Pass')),
                ('cerveza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cerveza')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]