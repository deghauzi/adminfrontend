# Generated by Django 3.2.9 on 2022-04-27 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('request_reasons', models.TextField(help_text='reason for withdrawal')),
                ('request_expected_date', models.CharField(max_length=12)),
                ('request_proccessed', models.BooleanField(default=False)),
                ('request_from_account', models.CharField(choices=[('Main', 'Main'), ('Wallet', 'Wallet')], max_length=20)),
                ('TransID', models.CharField(default='', max_length=12)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('request_proccessed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_proccessed_by', to=settings.AUTH_USER_MODEL)),
                ('request_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_withdrawal', to=settings.AUTH_USER_MODEL)),
                ('request_user_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_withdrawal_acc', to='account.bankaccount')),
            ],
            options={
                'verbose_name_plural': 'Withdrawal Request',
                'ordering': ['-created'],
            },
        ),
    ]
