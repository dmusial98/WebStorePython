# Generated by Django 4.0.2 on 2022-02-13 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('count', models.PositiveIntegerField()),
                ('cartId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='carts.cart')),
            ],
        ),
    ]
