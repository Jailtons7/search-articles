# Generated by Django 4.0 on 2021-12-29 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tblorgaoieexerc',
            old_name='codSiglaOrgaoIE',
            new_name='CodSiglaOrgaoIE',
        ),
        migrations.RenameField(
            model_name='tblorgaoieexerc',
            old_name='nomOrgaoIEExerc',
            new_name='NomOrgaoIEExerc',
        ),
    ]