# Generated by Django 4.1.4 on 2024-11-08 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('full_value', models.DecimalField(decimal_places=2, max_digits=50)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.products')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('valor_final', models.DecimalField(decimal_places=2, max_digits=99)),
                ('pay', models.DecimalField(decimal_places=0, max_digits=99)),
                ('change', models.DecimalField(decimal_places=0, default=0, max_digits=99)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers_app.customer')),
                ('products', models.ManyToManyField(through='sales_app.SaleProduct', to='products_app.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_app.sales'),
        ),
    ]