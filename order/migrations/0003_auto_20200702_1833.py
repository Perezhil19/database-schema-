# Generated by Django 2.1.11 on 2020-07-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200702_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
