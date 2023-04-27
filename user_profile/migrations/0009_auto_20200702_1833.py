# Generated by Django 2.1.11 on 2020-07-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20190913_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='deactivateuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='smsverification',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
