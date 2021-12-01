# Generated by Django 3.2.9 on 2021-12-01 22:45

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
            name='TargetContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('contribution_type', models.PositiveSmallIntegerField(choices=[(1, 'End of the Year Contribution'), (2, 'Sallah Contribution'), (3, 'Hajj/Umrah Pilgrimage'), (4, 'Jerusalem Pilgrimage'), (5, 'Car Facility'), (6, 'Mortgage Facilty')])),
                ('transaction_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Interest')], null=True)),
                ('contribution_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('contribution_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_attached_account', to='account.bankaccount')),
                ('created_by_admin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_admin_user_target', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contribution_acc', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Target Contributions',
            },
        ),
        migrations.CreateModel(
            name='DailyContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance_after_transaction', models.DecimalField(blank=True, decimal_places=2, help_text='please leave blank it auto generated', max_digits=12, null=True)),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Interest')])),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account.bankaccount')),
                ('created_by_admin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_admin_user_transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Daily Contributions',
                'ordering': ['-created'],
            },
        ),
    ]