# Generated by Django 3.2 on 2023-08-04 05:43

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
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('first_name', models.CharField(blank=True, default='update your account', max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, default='update your account', max_length=64, null=True)),
                ('email_address', models.CharField(blank=True, default='update your account', max_length=64, null=True)),
                ('country', models.CharField(blank=True, default='update your account', max_length=64, null=True)),
                ('home_address', models.CharField(blank=True, default='update your account', max_length=64, null=True)),
                ('code', models.CharField(blank=True, max_length=12)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deposit', models.FloatField(default=0, null=True)),
                ('balance', models.FloatField(default=0, null=True)),
                ('withdrawal', models.FloatField(default=0, null=True)),
                ('profit', models.FloatField(default=0, null=True)),
                ('roi', models.FloatField(default=0.015, null=True)),
                ('running_days', models.IntegerField(default=0, null=True)),
                ('wallet_address', models.CharField(default='update your account', max_length=400, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ref_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maximum_withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum_withdrawal', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Minimum_withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_withdrawal', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_username', models.CharField(max_length=200, null=True)),
                ('client_email', models.CharField(max_length=200, null=True)),
                ('transaction_hash', models.CharField(max_length=20, null=True)),
                ('crypto_used_for_requesting_withdrawal', models.CharField(max_length=35, null=True)),
                ('withdrawal_address', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField(default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomura_app.client')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, max_length=64, null=True)),
                ('transaction_id', models.CharField(blank=True, default='504ID.omit', max_length=30, null=True)),
                ('investment_plan', models.CharField(blank=True, default='504Package.omit', max_length=64, null=True)),
                ('amount', models.FloatField(default=0, null=True)),
                ('status', models.CharField(blank=True, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomura_app.client')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200, null=True)),
                ('price_amount', models.CharField(max_length=200, null=True)),
                ('investment_plan', models.FloatField(default=0.0052, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomura_app.client')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, default='Pending Bonus', max_length=64, null=True)),
                ('amount', models.FloatField(default=0, null=True)),
                ('code', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('client_email', models.CharField(blank=True, max_length=68, null=True)),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomura_app.client')),
            ],
        ),
    ]
