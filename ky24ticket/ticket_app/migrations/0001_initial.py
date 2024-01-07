# Generated by Django 5.0.1 on 2024-01-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(blank=True, max_length=20, null=True)),
                ('day', models.PositiveIntegerField(blank=True, choices=[(None, 'day'), (1, '1'), (2, '2'), (3, '3')], null=True)),
                ('entry_done', models.BooleanField(default=False)),
            ],
        ),
    ]
