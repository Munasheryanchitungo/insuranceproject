# Generated by Django 5.2.3 on 2025-06-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('mobile_money', 'Mobile Money'), ('bank_transfer', 'Bank Transfer'), ('cash', 'Cash Payment')], max_length=20)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('is_successful', models.BooleanField(default=False)),
            ],
        ),
    ]
