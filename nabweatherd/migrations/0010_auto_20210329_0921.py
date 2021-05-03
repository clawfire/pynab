# Generated by Django 3.0.7 on 2021-03-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nabweatherd", "0009_config_next_performance_weather_vocal"),
    ]

    operations = [
        migrations.RenameField(
            model_name="config",
            old_name="next_performance_weather_vocal",
            new_name="next_performance_weather_vocal_date",
        ),
        migrations.AddField(
            model_name="config",
            name="next_performance_weather_vocal_flag",
            field=models.IntegerField(default=0),
        ),
    ]
