# Generated by Django 5.0.4 on 2025-05-01 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0091_alter_stripepayment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stripepayment',
            options={'ordering': ['-created_at']},
        ),
    ]
