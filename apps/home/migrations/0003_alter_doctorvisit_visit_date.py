# Generated by Django 4.0.3 on 2022-04-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220409_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorvisit',
            name='visit_date',
            field=models.DateField(verbose_name='Visit Date'),
        ),
    ]