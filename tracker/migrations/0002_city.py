# Generated by Django 3.2 on 2021-04-22 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='tracker.state')),
            ],
        ),
    ]
