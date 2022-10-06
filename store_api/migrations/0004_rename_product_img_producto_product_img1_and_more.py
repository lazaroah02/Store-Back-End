# Generated by Django 4.0.4 on 2022-09-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0003_alter_categoria_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='product_img',
            new_name='product_img1',
        ),
        migrations.AddField(
            model_name='producto',
            name='product_img2',
            field=models.ImageField(default='productos_images/blank.png', upload_to='productos_images'),
        ),
        migrations.AddField(
            model_name='producto',
            name='product_img3',
            field=models.ImageField(default='productos_images/blank.png', upload_to='productos_images'),
        ),
    ]