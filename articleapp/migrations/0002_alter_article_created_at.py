# Generated by Django 4.1.5 on 2023-02-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]