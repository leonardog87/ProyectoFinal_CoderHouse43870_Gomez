# Generated by Django 4.2.3 on 2023-09-06 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0030_rename_mensaje_mensaje_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='AppWeb.blog'),
        ),
    ]
