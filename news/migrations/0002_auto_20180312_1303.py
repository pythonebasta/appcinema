# Generated by Django 2.0.3 on 2018-03-12 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='giornalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Giornalista'),
        ),
    ]
