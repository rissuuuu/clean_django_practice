# Generated by Django 3.2.5 on 2021-07-20 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealer', '0001_initial'),
        ('bottler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealerbrand',
            name='dealer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealer'),
        ),
        migrations.AddField(
            model_name='brand',
            name='bottler_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bottler.bottler'),
        ),
    ]
