# Generated by Django 5.0.1 on 2024-02-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0003_photography_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photography",
            name="category",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("ESTRELA", "Estrela"),
                    ("GALÁXIA", "Galáxia"),
                    ("PLANETA", "Planeta"),
                ],
                default="",
                max_length=15,
            ),
        ),
    ]
