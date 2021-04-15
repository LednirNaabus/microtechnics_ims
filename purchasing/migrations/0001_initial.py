# Generated by Django 3.1.7 on 2021-04-15 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import purchasing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasing',
            fields=[
                ('purchase_num', models.CharField(default=purchasing.models.generate_uuid, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('items', models.JSONField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'For Approval'), (2, 'Approved')], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('approved_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved', to=settings.AUTH_USER_MODEL)),
                ('requested_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
