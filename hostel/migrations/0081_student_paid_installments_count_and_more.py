# Generated by Django 5.0.4 on 2025-04-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0080_alter_payment_payment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='paid_installments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='partially_paid_installments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Amount_Paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Fee_Status',
            field=models.CharField(choices=[('PAID', 'Paid'), ('UNPAID', 'Unpaid'), ('PARTIALLY_PAID', 'Partially Paid'), ('PENDING', 'Pending')], default='UNPAID', max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Payment_Mode',
            field=models.CharField(blank=True, choices=[('CASH', 'Cash'), ('ONLINE', 'Online'), ('BANK', 'Bank'), ('CHEQUE', 'Cheque'), ('BANK_TRANSFER', 'Bank Transfer')], max_length=50, null=True),
        ),
    ]
