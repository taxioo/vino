# Generated by Django 3.2.6 on 2021-08-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
                ('wine_type', models.CharField(max_length=50)),
                ('sugar', models.IntegerField()),
                ('sour', models.IntegerField()),
                ('kind', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=100)),
                ('explain', models.CharField(max_length=500)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wine.country')),
            ],
        ),
    ]
