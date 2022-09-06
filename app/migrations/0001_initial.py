# Generated by Django 3.2 on 2022-07-07 10:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('contact', models.CharField(max_length=13)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Add Agent',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('account', models.IntegerField()),
                ('contact', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=150, null=True)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Add Brand',
                'verbose_name_plural': 'Add Brands',
            },
        ),
        migrations.CreateModel(
            name='CashInHandPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CheckCashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ChequeLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('total_amount', models.FloatField(blank=True, default=0)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=13)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Add Company',
                'verbose_name_plural': 'Add Companys',
            },
        ),
        migrations.CreateModel(
            name='DirectCompanyRecieve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, default='none5lucky-cement', null=True)),
                ('orderStatus', models.CharField(choices=[('Pending', 'Pending'), ('Received', 'Received'), ('Dispatched', 'Dispatched')], default='Pending', max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('FrieghtPerTon', models.FloatField(null=True)),
                ('Frieght_left', models.FloatField(blank=True, null=True)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('company_lg_id', models.IntegerField(blank=True, null=True)),
                ('wareHouse_lg_id', models.IntegerField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vihical_no', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=13)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Add Driver',
            },
        ),
        migrations.CreateModel(
            name='ExpenseHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FUCashFLow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('orderStatus', models.CharField(choices=[('Pending', 'Pending'), ('Received', 'Received')], default='Pending', max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('Frieght', models.FloatField(null=True)),
                ('unloading', models.FloatField(null=True)),
                ('Frieght_left', models.FloatField(blank=True, null=True)),
                ('unloading_left', models.FloatField(blank=True, null=True)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('company_lg_id', models.IntegerField(blank=True, null=True)),
                ('wareHouse_lg_id', models.IntegerField(blank=True, null=True)),
                ('fu_lg_id', models.IntegerField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('contact', models.CharField(max_length=13)),
                ('opening_Balance', models.FloatField()),
                ('current_Balance', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Add Party',
                'verbose_name_plural': 'Add Parties',
            },
        ),
        migrations.CreateModel(
            name='WareHouseEnventoryLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True)),
                ('directCompany_id', models.IntegerField(blank=True, null=True)),
                ('qty', models.IntegerField()),
                ('rate', models.FloatField()),
                ('description', models.CharField(max_length=50, null=True)),
                ('is_DCR', models.BooleanField(blank=True, default=False)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField(null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Cheque', 'Cheque')], max_length=10)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('recived_amount', models.FloatField()),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('cheque_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='PayToParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Party', 'Party'), ('Cheque', 'Cheque'), ('Agent', 'Agent')], max_length=10)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('recived_amount', models.FloatField()),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('party2_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('cheque_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.party')),
                ('party_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Part_2', to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='PayToCashInHandPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Bank', 'Bank'), ('Party', 'Party'), ('Agent', 'Agent')], max_length=10)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('recived_amount', models.FloatField()),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('cash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cashinhandperson')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='PayToBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Party', 'Party'), ('Cheque', 'Cheque'), ('Agent', 'Agent')], max_length=10)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('recived_amount', models.FloatField()),
                ('cheque_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank2_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('bank_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bank_2', to='app.bank')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='PayToAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Party', 'Party'), ('Cheque', 'Cheque'), ('Agent', 'Agent')], max_length=10)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('recived_amount', models.FloatField()),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('agent2_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('cheque_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('agent_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent2', to='app.agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='PartyLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('qty', models.IntegerField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('totalFrieght', models.FloatField(null=True)),
                ('totalUnloading', models.FloatField(null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField(null=True)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='PartiesTranspotationManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True)),
                ('qty', models.IntegerField()),
                ('friegth', models.FloatField(blank=True, default=0)),
                ('unloading', models.FloatField(blank=True, default=0)),
                ('fu_lg_id', models.IntegerField(blank=True, null=True)),
                ('driver_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('directCompanyRecieve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.directcompanyrecieve')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
                ('orderPlacement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.orderplacement')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='FriegthUnloadingLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('friegth', models.FloatField(blank=True, default=0)),
                ('unloading', models.FloatField(blank=True, default=0)),
                ('qty', models.IntegerField(default=0)),
                ('total_amount', models.FloatField(null=True)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('cashFlow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fucashflow')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, null=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField(blank=True, default=0)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('expenseHead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.expensehead')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Agent', 'Agent'), ('Party', 'Party')], max_length=10)),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('amount', models.FloatField()),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('expense_lg_id', models.IntegerField(blank=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('expenseHead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.expensehead')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='ExpectedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_orders', models.IntegerField()),
                ('expected_rate', models.FloatField()),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='DriverReceiving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, null=True)),
                ('total_amount', models.FloatField()),
                ('driver_lg_id', models.IntegerField(blank=True, null=True)),
                ('fu_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, null=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('qty', models.FloatField(default=0)),
                ('friegth', models.FloatField(blank=True, default=0)),
                ('unloading', models.FloatField(blank=True, default=0)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('total_amount', models.FloatField(blank=True, default=0)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DispatchEnventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('qty', models.IntegerField()),
                ('rate', models.FloatField()),
                ('destination', models.CharField(max_length=100)),
                ('totalAmount', models.FloatField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('warehouse_lg_id', models.IntegerField(blank=True, null=True)),
                ('driver_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.brand')),
                ('driver', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('qty', models.IntegerField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('total_Frieght', models.FloatField(null=True)),
                ('total_Unloading', models.FloatField(null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField(blank=True, default=0.0)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, null=True)),
                ('chequeStatus', models.CharField(choices=[('Pending', 'Pending'), ('Bounced', 'Bounced'), ('BankDeposited', 'BankDeposited'), ('Withdrawn', 'Withdrawn')], default='Pending', max_length=50)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField()),
                ('cheque_lg_id', models.IntegerField(blank=True, null=True)),
                ('company_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='CashLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('cashInHandPerson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cashinhandperson')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Bank', 'Bank'), ('Agent', 'Agent'), ('Party', 'Party')], max_length=10)),
                ('amount_paid', models.FloatField()),
                ('company_lg_id', models.IntegerField(blank=True, null=True)),
                ('bank_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('cheque_id', models.IntegerField(blank=True, null=True)),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('party_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.party')),
            ],
        ),
        migrations.CreateModel(
            name='BankLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('total_amount', models.FloatField(null=True)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
            ],
        ),
        migrations.CreateModel(
            name='AgentReceiving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('received_amount', models.FloatField()),
                ('agent_lg_id', models.IntegerField(blank=True, null=True)),
                ('cash_lg_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
            ],
        ),
        migrations.CreateModel(
            name='AgentLeadger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, null=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('total_amount', models.FloatField(blank=True, default=0)),
                ('net_Balancse', models.FloatField(blank=True, default=0.0)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
            ],
        ),
    ]
