# Generated by Django 4.0 on 2022-01-02 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tblidioma_tblartigopublicado_codidioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblartigopublicado',
            name='CodServidor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='api.tblservidores'),
            preserve_default=False,
        ),
    ]