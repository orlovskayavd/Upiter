# Generated by Django 3.2.16 on 2024-05-14 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20240514_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armenia',
            name='Producer_tran',
        ),
        migrations.RemoveField(
            model_name='armenia',
            name='Registrator_country',
        ),
        migrations.RemoveField(
            model_name='armenia',
            name='Sc_name',
        ),
        migrations.RemoveField(
            model_name='grls',
            name='Producer_tran',
        ),
        migrations.RemoveField(
            model_name='grls',
            name='Registrator_country',
        ),
        migrations.RemoveField(
            model_name='grls',
            name='Sc_name',
        ),
        migrations.RemoveField(
            model_name='kazakhstan',
            name='Registrator_country',
        ),
        migrations.RemoveField(
            model_name='kazakhstan',
            name='Registrator_tran',
        ),
        migrations.RemoveField(
            model_name='kazakhstan',
            name='Sc_name',
        ),
        migrations.RemoveField(
            model_name='kyrgyzstan',
            name='Registrator_country',
        ),
        migrations.RemoveField(
            model_name='kyrgyzstan',
            name='Registrator_tran',
        ),
        migrations.RemoveField(
            model_name='kyrgyzstan',
            name='Sc_name',
        ),
    ]