# Generated by Django 4.0.4 on 2022-06-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_alter_product_prod_img_back_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img_main',
            field=models.ImageField(blank=True, default='', upload_to='prod_img'),
        ),
    ]