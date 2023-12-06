# Generated by Django 4.2 on 2023-12-06 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0003_alter_player_moonsigninterpretation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moonsigninterpretation",
            name="on_player",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="game.player",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="MoonSignInterpretation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="game.moonsigninterpretation",
            ),
        ),
    ]