# Generated by Django 5.0.1 on 2024-03-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_customer_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
