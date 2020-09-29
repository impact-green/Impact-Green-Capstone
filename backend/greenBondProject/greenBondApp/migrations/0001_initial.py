# Generated by Django 3.1.1 on 2020-09-29 20:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SDG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('official_description', models.CharField(max_length=10000)),
                ('original_description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('project_number', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('sdg', models.ManyToManyField(to='greenBondApp.SDG')),
            ],
        ),
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('enterprise', models.CharField(choices=[('Water', 'Water'), ('Power', 'Power'), ('Waste Water', 'Waste Water')], max_length=100)),
                ('issue_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(3000)])),
                ('series', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[A-Z]$')])),
                ('bond_type', models.CharField(choices=[('Revenue', 'Revenue'), ('Refunding', 'Refunding')], max_length=100)),
                ('CUSIP', models.CharField(max_length=100)),
                ('avg_mature_rate', models.DecimalField(decimal_places=4, max_digits=5)),
                ('project', models.ManyToManyField(to='greenBondApp.Project')),
            ],
        ),
    ]