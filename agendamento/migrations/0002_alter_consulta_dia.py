# Generated by Django 5.0.6 on 2024-06-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='dia',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]