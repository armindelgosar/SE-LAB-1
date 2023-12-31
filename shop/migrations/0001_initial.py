# Generated by Django 4.2.6 on 2023-10-28 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('delivery_duration', models.DurationField()),
                ('delivery_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('DELIVERED', 'DELIVERED'), ('PICKED', 'PICKED'), ('ASSIGNED', 'ASSIGNED'), ('AT_VENDOR', 'AT_VENDOR')], default='AT_VENDOR', max_length=16)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip', to='shop.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.vendor'),
        ),
        migrations.CreateModel(
            name='DelayReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=16)),
                ('result', models.CharField(choices=[('ADDED_TO_DELAY_QUEUE', 'ADDED_TO_DELAY_QUEUE'), ('DURATION_UPDATED', 'DURATION_UPDATED')], max_length=32)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delay_reports', to='shop.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DelayQueueItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='queue_item', to='shop.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=16)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='shop.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
