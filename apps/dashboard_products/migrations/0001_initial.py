# Generated by Django 4.1.4 on 2024-11-08 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_statistics', models.CharField(blank=True, max_length=50)),
                ('product_image_statistics', models.ImageField(blank=True, upload_to='stats_products')),
                ('quantity_statistics', models.PositiveIntegerField()),
                ('sold_value', models.DecimalField(decimal_places=0, max_digits=99)),
                ('revenue', models.DecimalField(decimal_places=0, max_digits=99)),
                ('code_statistics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.products')),
            ],
        ),
    ]
