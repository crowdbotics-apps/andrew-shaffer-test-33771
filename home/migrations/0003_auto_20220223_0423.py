# Generated by Django 2.2.27 on 2022-02-23 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_app_plan_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='app',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.App'),
        ),
    ]