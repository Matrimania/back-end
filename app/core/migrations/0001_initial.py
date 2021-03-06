# Generated by Django 3.1.5 on 2021-01-12 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('guest', models.ManyToManyField(to='core.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('image', models.CharField(default='https://images.unsplash.com/reserve/xd45Y326SvKzSR3Nanc8_MRJ_8125-1.jpg?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeddingGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guest')),
                ('wedding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.wedding')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guest')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.photo')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='wedding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.wedding'),
        ),
        migrations.AddField(
            model_name='guest',
            name='wedding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.wedding'),
        ),
    ]
