# Generated by Django 5.0.6 on 2024-07-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0002_alter_transaction_bank_account_creditcard_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bank",
            name="color",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
