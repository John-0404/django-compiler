# Generated by Django 3.2.4 on 2021-08-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0004_alter_getinfor_namefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='getinfor',
            name='Res',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='getinfor',
            name='parameter',
            field=models.TextField(null=True),
        ),
    ]