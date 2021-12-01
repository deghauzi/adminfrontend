# Generated by Django 3.2.9 on 2021-12-01 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('request_reasons', models.TextField(help_text='reason for withdrawal')),
                ('request_date', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('request_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_withdrawal', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Withdrawal Request',
                'ordering': ['-created'],
            },
        ),
    ]
