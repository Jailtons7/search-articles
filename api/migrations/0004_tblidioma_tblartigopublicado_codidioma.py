# Generated by Django 4.0 on 2022-01-02 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_tblarea_id_remove_tblespecialidade_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblIdioma',
            fields=[
                ('CodIdioma', models.AutoField(primary_key=True, serialize=False)),
                ('DscIdioma', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
            },
        ),
        migrations.AddField(
            model_name='tblartigopublicado',
            name='CodIdioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tblidioma'),
        ),
    ]