# Generated by Django 2.0.2 on 2019-11-24 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidder', models.CharField(max_length=200)),
                ('bid_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('vehicle_model', models.CharField(max_length=200)),
                ('vehicle_age', models.CharField(default='1 year', max_length=200)),
                ('vehicle_image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('active_status', models.BooleanField(default=True)),
                ('vehicle_km', models.IntegerField()),
                ('text', models.TextField()),
                ('vr_image', models.ImageField(upload_to='vr_uploads/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bids',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='portal.Post'),
        ),
    ]
