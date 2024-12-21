# Generated by Django 5.1.4 on 2024-12-17 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Raw Material',
                'verbose_name_plural': 'Raw Materials',
                'db_table': 'raw_materials',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='raw_material_name_idx')],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'db_table': 'suppliers',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='supplier_name_idx')],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pre_quantity', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('change_type', models.CharField(choices=[('IN', 'In'), ('OUT', 'Out'), ('RETURNED', 'Returned'), ('DISCARDED', 'Discarded')], max_length=10)),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.rawmaterial')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'db_table': 'stocks',
                'ordering': ['store', 'raw_material', 'change_type'],
                'indexes': [models.Index(fields=['store'], name='stock_store_idx'), models.Index(fields=['raw_material'], name='stock_raw_material_idx')],
            },
        ),
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('UNCONFIRMED', 'Unconfirmed'), ('CONFIRMED', 'Confirmed'), ('PREPARING', 'Preparing'), ('SHIPPING', 'Shipping'), ('RECEIVED', 'Received'), ('REJECTED', 'Rejected')], default='UNCONFIRMED', max_length=11)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.employee')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.rawmaterial')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.supplier')),
            ],
            options={
                'verbose_name': 'Order Record',
                'verbose_name_plural': 'Order Records',
                'db_table': 'order_records',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['employee'], name='order_employee_idx'), models.Index(fields=['supplier'], name='order_supplier_idx'), models.Index(fields=['status'], name='order_status_idx')],
            },
        ),
    ]
