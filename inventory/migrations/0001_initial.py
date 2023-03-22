# Generated by Django 3.2.8 on 2022-10-12 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img', models.ImageField(blank=True, null=True, upload_to='Category')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentform', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img', models.ImageField(blank=True, null=True, upload_to='Subcategory')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_order', models.IntegerField(default=0)),
                ('code_product', models.IntegerField()),
                ('product', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quanty', models.IntegerField(default=0)),
                ('coupon', models.CharField(max_length=10)),
                ('shipping', models.FloatField()),
                ('description', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('payment_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_buyls', to='inventory.paymentform')),
                ('user_buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_buyls', to='user.user')),
                ('user_sells', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sells', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quanty', models.IntegerField()),
                ('img', models.ImageField(upload_to='Product')),
                ('description', models.TextField()),
                ('state', models.IntegerField()),
                ('shipping_price', models.FloatField(default=0.0)),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.subcategories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Product_Photos')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Consecutive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]