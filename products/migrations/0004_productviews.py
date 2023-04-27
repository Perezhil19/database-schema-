# Generated by Django 2.2.4 on 2019-08-13 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190811_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_views', to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
