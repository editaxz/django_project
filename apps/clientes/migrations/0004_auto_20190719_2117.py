# Generated by Django 2.0.7 on 2019-07-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190719_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='apellido',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]