# Generated by Django 2.2.10 on 2020-07-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200716_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport Wear'), ('OW', 'Outwear'), ('GP', 'Gents Pants'), ('LP', 'Ladies Pants'), ('T', 'Tshirts'), ('C', 'Coat'), ('LT', 'Ladies Tops'), ('LS', 'Ladies Shirt')], max_length=2),
        ),
    ]
