# Generated by Django 4.2.3 on 2023-09-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_leader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='image',
            field=models.ImageField(blank='True', default='default.jpg', null=True, upload_to='leader_images/'),
        ),
    ]
