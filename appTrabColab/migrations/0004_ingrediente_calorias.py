# Generated by Django 2.2.7 on 2019-11-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTrabColab', '0003_auto_20191112_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='calorias',
            field=models.IntegerField(default=0),
        ),
    ]