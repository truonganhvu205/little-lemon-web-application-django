# Generated by Django 5.0 on 2023-12-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_booking_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
    ]
