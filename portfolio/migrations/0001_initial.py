# Generated by Django 5.1.3 on 2024-12-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='media/portfolio_thumbs')),
                ('status', models.CharField(choices=[('personal', 'Personal'), ('exploration', 'Exploration'), ('commercial', 'Commecrial')], default='personal', max_length=20)),
                ('tags', models.ManyToManyField(to='portfolio.projecttag')),
            ],
        ),
    ]
