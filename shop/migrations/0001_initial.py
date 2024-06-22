# Generated by Django 4.2 on 2024-06-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Category Title')),
                ('is_active', models.BooleanField(verbose_name='Active / Unactive')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category List',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Product Title')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('short_description', models.CharField(max_length=400, null=True, verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(blank=True, default='', unique=True, verbose_name='Title in url')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active / Unactive')),
                ('category', models.ManyToManyField(to='shop.productcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product List',
            },
        ),
    ]
