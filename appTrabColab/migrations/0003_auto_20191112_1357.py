# Generated by Django 2.2.7 on 2019-11-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTrabColab', '0002_pizza_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='ingredientes',
            field=models.ManyToManyField(to='appTrabColab.Ingrediente'),
        ),
        migrations.DeleteModel(
            name='IngredientePizza',
        ),
    ]