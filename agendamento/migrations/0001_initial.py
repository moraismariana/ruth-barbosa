# Generated by Django 5.0.6 on 2024-06-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(choices=[('CLAREAMENTO DENTAL', 'Clareamento dental'), ('FACETAS', 'Facetas'), ('LENTES DE CONTATO', 'Lentes de Contato'), ('TRATAMENTO DE CANAL', 'Tratamento de Canal'), ('TRATAMENTO DE GENGIVA', 'Tratamento de Gengiva')], max_length=100)),
                ('mes', models.CharField(choices=[('JUNHO', 'Junho'), ('JULHO', 'Julho'), ('AGOSTO', 'Agosto')], max_length=20)),
                ('dia', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2)),
                ('horario', models.TimeField(max_length=100)),
            ],
        ),
    ]
