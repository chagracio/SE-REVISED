# Generated by Django 4.1.4 on 2022-12-09 11:21

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
            name='Barangay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('shippingFee', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('ContactNum', models.CharField(max_length=11, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_id', models.ImageField(null=True, upload_to='customer_ids/')),
                ('loan', models.BooleanField(default=False, null=True)),
                ('barangay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.barangay')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('loanPrice', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('image', models.ImageField(null=True, upload_to='rice_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingMeth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_paid', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.order')),
                ('rice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.riceitem')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('shippingMeth', models.CharField(max_length=15, null=True)),
                ('loan', models.BooleanField(default=False, null=True)),
                ('shippingStatus', models.CharField(blank=True, choices=[('Preparing', 'Preparing'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Ready for Pick Up', 'YReady for Pick Up'), ('Picked Up', 'Picked Up')], max_length=50)),
                ('orderStatus', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Denied', 'Denied')], max_length=50)),
                ('cancel', models.BooleanField(default=False, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.order')),
                ('rice_ordered', models.ManyToManyField(blank=True, related_name='orders', to='customer.orderriceitems')),
            ],
        ),
        migrations.CreateModel(
            name='LendingStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('total_amount_paid', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=10, null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.shippingmeth'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]