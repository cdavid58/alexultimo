# Generated by Django 3.2.8 on 2022-10-12 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('second_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('last_second_name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('code_area', models.CharField(blank=True, max_length=5)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('user', models.CharField(max_length=50)),
                ('pswd', models.CharField(max_length=50)),
                ('img_profile', models.ImageField(blank=True, default='Img_Profile/without.jpg', upload_to='Img_Profile')),
                ('img_cover', models.ImageField(blank=True, default='Img_Cover/cover.jpg', upload_to='Img_Cover')),
                ('description', models.TextField(blank=True)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('cargo', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('froms', models.CharField(max_length=10)),
                ('to', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Tag_You',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alls', models.BooleanField(default=True)),
                ('group', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('receiving_user', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='See_Your_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alls', models.BooleanField(default=True)),
                ('followers', models.BooleanField(default=False)),
                ('only_me', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=150)),
                ('titulo', models.CharField(max_length=150)),
                ('froms', models.CharField(max_length=10)),
                ('to', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Account_Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_followers', models.BooleanField(default=True)),
                ('show_emai', models.BooleanField(default=True)),
                ('show_experiences', models.BooleanField(default=True)),
                ('show_number_phone', models.BooleanField(default=True)),
                ('show_follow_you', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
