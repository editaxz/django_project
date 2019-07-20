# Generated by Django 2.0.7 on 2019-07-20 01:57

import clientes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20190718_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes_Consolidados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='clientes',
            name='file',
            field=models.FileField(default='', upload_to='', validators=[clientes.models.Clientes.validar_archivo]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientes_consolidados',
            name='relacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Clientes'),
        ),
    ]
