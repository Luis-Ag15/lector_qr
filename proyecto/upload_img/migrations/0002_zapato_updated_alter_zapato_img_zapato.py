# Generated by Django 4.2.5 on 2023-09-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_img', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapato',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='zapato',
            name='img_zapato',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
