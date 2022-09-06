from re import T
from django import utils
from django.db import models
from django.template.defaultfilters import  slugify
import random
import string
# Create your models here.
from django.utils import timezone
# Self Define Function
from utils.utils import ConsignmentAmount, DeleteLeadgers, UpdateLeadgers
from .import static
#shkjahdkjahsdkjahsd

class Company(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Add Company'
        verbose_name_plural = 'Add Companys'

# UI


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Add Brand'
        verbose_name_plural = 'Add Brands'

# UI



class Party(models.Model):
    name = models.CharField(max_length=30, unique=True)
    contact = models.CharField(max_length=13)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance

        super(Party, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Add Party'
        verbose_name_plural = 'Add Parties'


# UI


class Agent(models.Model):
    name = models.CharField(max_length=30, unique=True)
    contact = models.CharField(max_length=13)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(Agent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Add Agent'

# UI


class Driver(models.Model):
    name = models.CharField(max_length=30)
    vihical_no = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Add Driver'

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(Driver, self).save(*args, **kwargs)


# UI


class CashInHandPerson(models.Model):
    name = models.CharField(max_length=30)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(CashInHandPerson, self).save(*args, **kwargs)


# UI

class CheckCashFlow(models.Model):
    name = models.CharField(max_length=30)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(CheckCashFlow, self).save(*args, **kwargs)
# UI


class FUCashFLow(models.Model):
    name = models.CharField(max_length=30)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(FUCashFLow, self).save(*args, **kwargs)


# Ui
class ExpenseHead(models.Model):
    name = models.CharField(max_length=150)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(ExpenseHead, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# UI


class Bank(models.Model):
    name = models.CharField(max_length=30, unique=True)
    account = models.IntegerField()
    contact = models.CharField(max_length=13)
    address = models.CharField(null=True, max_length=150)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(Bank, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Enventory & leadger


class WareHouseEnventoryLeadger(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    directCompany_id = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField()
    rate = models.FloatField()
    description = models.CharField(max_length=50, null=True)
    is_DCR = models.BooleanField(default=False, blank=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(null=True)


# Leadgers

class BankLeadger(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    description = models.CharField(max_length=50, null=True, blank=True)
    total_amount = models.FloatField(null=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        b = Bank.objects.get(id=self.bank.id)
        if self.id == None:
            if self.transaction_type == 'Credit':
                b.current_Balance -= self.total_amount
                self.net_Balancse = b.current_Balance
            else:
                b.current_Balance += self.total_amount
                self.net_Balancse = b.current_Balance
            b.save()
            super(BankLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, BankLeadger, 'Bank', True)
                obj.total_amount = self.total_amount
                obj.description = self.description

            super(BankLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, BankLeadger, 'Bank', True)
        else:
            super(BankLeadger, self).delete()


class FriegthUnloadingLeadger(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    cashFlow = models.ForeignKey(FUCashFLow, on_delete=models.CASCADE)
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    description = models.CharField(max_length=50, null=True, blank=True)
    friegth = models.FloatField(blank=True, default=0)
    unloading = models.FloatField(blank=True, default=0)
    qty = models.IntegerField(default=0)
    total_amount = models.FloatField(null=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        p = FUCashFLow.objects.all()
        if len(p) == 0:
            p = FUCashFLow(name='Frieght_Unloading', opening_Balance=0)
            p.save()
        else:
            p = p[0]
        self.cashFlow = p
        if self.id == None:
            if self.transaction_type == 'Credit':
                p.current_Balance -= self.total_amount
                self.net_Balancse = p.current_Balance
            else:
                p.current_Balance += self.total_amount
                self.net_Balancse = p.current_Balance
            p.save()
            super(FriegthUnloadingLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(
                    self, FriegthUnloadingLeadger, 'FU', True)
                obj.total_amount = self.total_amount
                obj.description = self.description
                obj.qty = self.qty
                obj.friegth = self.friegth
                obj.party = self.party
                obj.unloading = self.unloading
            super(FriegthUnloadingLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, FriegthUnloadingLeadger, 'FU', True)
        else:
            super(FriegthUnloadingLeadger, self).delete()


class CashLeadger(models.Model):
    cashInHandPerson = models.ForeignKey(
        CashInHandPerson, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now, blank=True)
    description = models.CharField(
        max_length=100, default='', blank=True, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(blank=True, null=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)

    def save(self, *args, **kwargs):
        c = CashInHandPerson.objects.all().first()
        if self.id == None:
            if self.transaction_type == 'Credit':
                c.current_Balance -= self.total_amount
                self.net_Balancse = c.current_Balance
            else:
                c.current_Balance += self.total_amount
                self.net_Balancse = c.current_Balance
            c.save()
            self.cashInHandPerson = c
            super(CashLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, CashLeadger, 'Cash', True)
                obj.total_amount = self.total_amount
                obj.description = self.description

            super(CashLeadger, obj).save(*args, **kwargs)

    def __str__(self):
        return self.cashInHandPerson.name

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, CashLeadger, 'Cash', True)
        else:
            super(CashLeadger, self).delete()


class CompanyLeadger(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    total_Frieght = models.FloatField(null=True)
    total_Unloading = models.FloatField(null=True)
    description = models.CharField(max_length=50, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(blank=True, default=0.0)
    net_Balancse = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.company.name + ' : ' + str(self.date)

    def save(self, *args, **kwargs):
        c = Company.objects.get(id=self.company.id)
        if self.id == None:
            if self.transaction_type == 'Credit':
                c.current_Balance += self.total_amount
                self.net_Balancse = c.current_Balance
            else:
                c.current_Balance -= self.total_amount
                self.net_Balancse = c.current_Balance
            c.save()
            super(CompanyLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, CompanyLeadger, 'Company',False)
                obj.brand = self.brand
                obj.qty = self.qty
                obj.rate = self.rate
                obj.total_Frieght = self.total_Frieght
                obj.total_Unloading = self.total_Unloading
                obj.description = self.description
                obj.total_amount = self.total_amount

            super(CompanyLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, CompanyLeadger, 'Company',False)
        else:
            super(CompanyLeadger, self).delete()


class PartyLeadger(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    totalFrieght = models.FloatField(null=True)
    totalUnloading = models.FloatField(null=True)
    description = models.CharField(max_length=50, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(null=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.party.name + str(self.id)

    def save(self, *args, **kwargs):
        p = Party.objects.get(id=self.party.id)
        if self.id == None:
            if self.transaction_type == 'Credit':
                p.current_Balance -= self.total_amount
                self.net_Balancse = p.current_Balance
            else:
                p.current_Balance += self.total_amount
                self.net_Balancse = p.current_Balance
            p.save()
            super(PartyLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, PartyLeadger, 'Party', True)
                obj.brand = self.brand
                obj.qty = self.qty
                obj.rate = self.rate
                obj.totalFrieght = self.totalFrieght
                obj.totalUnloading = self.totalUnloading
                obj.description = self.description
                obj.total_amount = self.total_amount

            super(PartyLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, PartyLeadger, 'Party', True)
        else:
            super(PartyLeadger, self).delete()


class AgentLeadger(models.Model):
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(default=0, blank=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.agent.name

    def save(self, *args, **kwargs):
        a = Agent.objects.get(id=self.agent.id)
        if self.id == None:
            if self.transaction_type == 'Credit':
                a.current_Balance -= self.total_amount
                self.net_Balancse = a.current_Balance
            else:
                a.current_Balance += self.total_amount
                self.net_Balancse = a.current_Balance
            a.save()
            super(AgentLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, AgentLeadger, 'Agent', True)
                obj.total_amount = self.total_amount
                obj.description = self.description

            super(AgentLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, AgentLeadger, 'Agent', True)
        else:
            super(AgentLeadger, self).delete()


class ExpenseLeadger(models.Model):
    expenseHead = models.ForeignKey(
        ExpenseHead, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(default=0, blank=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        e = ExpenseHead.objects.get(id=self.expenseHead.id)
        if self.id == None:
            if self.transaction_type == 'Credit':
                e.current_Balance -= self.total_amount
                self.net_Balancse = e.current_Balance
            else:
                e.current_Balance += self.total_amount
                self.net_Balancse = e.current_Balance
            e.save()
            super(ExpenseLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, ExpenseLeadger, 'Expense', True)
                obj.total_amount = self.total_amount
                obj.description = self.description
            super(ExpenseLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, ExpenseLeadger, 'Expense', True)
        else:
            super(ExpenseLeadger, self).delete()


class DriverLeadger(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    qty = models.FloatField(default=0)
    friegth = models.FloatField(blank=True, default=0)
    unloading = models.FloatField(blank=True, default=0)
    net_Balancse = models.FloatField(blank=True, default=0.0)
    total_amount = models.FloatField(default=0, blank=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        e = Driver.objects.get(id=self.driver.id)
        if self.id == None:
            if self.transaction_type == 'Credit':
                e.current_Balance += self.total_amount
                self.net_Balancse = e.current_Balance
            else:
                e.current_Balance -= self.total_amount
                self.net_Balancse = e.current_Balance
            e.save()
            super(DriverLeadger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, DriverLeadger, 'Driver')
                obj.qty = self.qty
                obj.frieght = self.friegth
                obj.unloading = self.unloading
                obj.description = self.description
                obj.total_amount = self.total_amount
            super(DriverLeadger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, DriverLeadger, 'Driver')
        else:
            super(DriverLeadger, self).delete()


class ChequeLeadger(models.Model):
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    description = models.CharField(max_length=50, null=True)
    total_amount = models.FloatField(default=0, blank=True)
    net_Balancse = models.FloatField(blank=True, default=0.0)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        e = CheckCashFlow.objects.first()
        if self.id == None:
            if self.transaction_type == 'Credit':
                e.current_Balance += self.total_amount
                self.net_Balancse = e.current_Balance
            else:
                e.current_Balance -= self.total_amount
                self.net_Balancse = e.current_Balance
            e.save()
            super(ChequeLeadger, self).save(*args, **kwargs)
        
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, ChequeLeadger, 'Cheque')
                obj.total_amount = self.total_amount

            super(ChequeLeadger, obj).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, ChequeLeadger, 'Cheque')
        else:
            super(ChequeLeadger, self).delete()

# UI


class Cheque(models.Model):
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True)
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=50, null=True)
    chequeStatus = models.CharField(max_length=50, choices=[(
        'Pending', 'Pending'), ('Bounced', 'Bounced'), ('BankDeposited', 'BankDeposited'), ('Withdrawn', 'Withdrawn')], default='Pending')
    transaction_type = models.CharField(
        max_length=50, choices=(('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField()
    cheque_lg_id = models.IntegerField(blank=True, null=True)
    company_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            cl = ChequeLeadger(transaction_type=self.transaction_type,
                               description=self.description, total_amount=self.total_amount)
            cl.save()
            self.cheque_lg_id = cl.id
        else:
            # Update Cheque Leadger
            cl = ChequeLeadger.objects.get(id=self.cheque_lg_id)
            cl.description = self.description
            cl.total_amount = self.total_amount
            cl.save()
           
            # Update Status
            if self.chequeStatus == 'Bounced':
                try:
                    if self.party_lg_id:
                        pl = PartyLeadger.objects.get(id=self.party_lg_id)
                        pl.party = self.party
                        pl.total_amount = self.total_amount
                        pl.description = self.description
                        pl.save()
                    else:
                        pl = PartyLeadger(party=self.party, transaction_type='Debit',
                                        total_amount=self.total_amount, description=self.description)
                        pl.save()
                        self.party_lg_id = pl.save()
                except:
                    if self.company_lg_id:
                        cl = CompanyLeadger.objects.get(id=self.company_lg_id)
                        cl.agent = self.agent
                        cl.company = self.company
                        cl.transaction_type = 'Debit'
                        cl.description = self.description
                        cl.total_amount = self.total_amount
                        cl.save()
                    else:
                        cm = CompanyLeadger(company=self.company, transaction_type='Credit',
                                description=self.description, total_amount=self.total_amount)
                        cm.save()
                        self.company_lg_id = cm.id
                        
            elif self.chequeStatus == 'BankDeposited':
                if self.bank_lg_id:
                    bl = BankLeadger.objects.get(id=self.bank_lg_id)
                    bl.bank = self.bank
                    bl.total_amount = self.total_amount
                    bl.description = self.description
                    bl.save()
                else:
                    bl = BankLeadger(bank=self.bank, transaction_type='Credit',
                                     total_amount=self.total_amount, description=self.description)
                    bl.save()
                    self.bank_lg_id = bl.id
            elif self.chequeStatus == 'Withdrawn':
                if self.cash_lg_id:
                    ch = CashLeadger.objects.get(id=self.cash_lg_id)
                    ch.descriptiom = self.description
                    ch.total_amount = self.total_amount
                    ch.save()
                else:
                    ch = CashLeadger(description=self.description,
                                     transaction_type='Debit', total_amount=self.total_amount)
                    ch.save()
                    self.cash_lg_id = ch.id
            if self.chequeStatus != 'Pending':
                cl = ChequeLeadger(transaction_type='Debit',
                                   description=self.description, total_amount=self.total_amount)
                cl.save()
                self.cheque_lg_id = cl.id
        super(Cheque, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.chequeStatus == 'Bounced':
            if self.party_lg_id:
                PartyLeadger.objects.get(id=self.party_lg_id).delete()
            else:
                CompanyLeadger.objects.get(id=self.company_lg_id).delete()
        elif self.chequeStatus == 'BankDeposited':
            BankLeadger.objects.get(id=self.bank_lg_id).delete()
        ChequeLeadger.objects.get(id=self.cheque_lg_id).delete()
        super(Cheque, self).delete()


# UI


class DriverReceiving(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)
    total_amount = models.FloatField()
    driver_lg_id = models.IntegerField(blank=True, null=True)
    fu_lg_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            d = DriverLeadger(driver=self.driver, description=self.description,
                              transaction_type='Debit', total_amount=self.total_amount)
            d.save()
            self.driver_lg_id = d.id
            fu = FriegthUnloadingLeadger(
                transaction_type='Credit', description=self.description, total_amount=self.total_amount)
            fu.save()
            self.fu_lg_id = fu.id
        else:
            d = DriverLeadger.objects.get(id=self.driver_lg_id)
            d.driver = self.driver
            d.description = self.description
            d.transaction_type = 'Debit'
            d.total_amount = self.total_amount
            d.save()

            fu = FriegthUnloadingLeadger.objects.get(id=self.fu_lg_id)
            fu.transaction_type = 'Credit'
            fu.description = self.description
            fu.total_amount = self.total_amount
            fu.save()

        super(DriverReceiving, self).save(*args, **kwargs)


# UI


class OrderPlacement(models.Model):
    
    date = models.DateField(default=timezone.now, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    orderStatus = models.CharField(max_length=50, choices=[(
        'Pending', 'Pending'), ('Received', 'Received')], default='Pending')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Destination = models.CharField(max_length=50)
    qty = models.IntegerField()
    rate = models.IntegerField()
    Frieght = models.FloatField(null=True)
    unloading = models.FloatField(null=True)
    Frieght_left = models.FloatField(null=True, blank=True)
    unloading_left = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    company_lg_id = models.IntegerField(blank=True, null=True)
    wareHouse_lg_id = models.IntegerField(blank=True, null=True)
    fu_lg_id = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if self.id == None:
            self.total_amount = (self.qty * self.rate)
            code = ''.join(random.choices(
                string.ascii_uppercase + self.company.name, k=10))
            self.slug = slugify(code)

            self.Frieght_left = self.Frieght
            self.unloading_left = self.unloading
            if self.orderStatus == 'Received':
                c = CompanyLeadger(company=self.company, brand=self.brand, qty=self.qty, rate=self.rate,
                                   total_Frieght=self.qty * self.Frieght, total_Unloading=self.qty*self.unloading, transaction_type='Credit',
                                   description=self.Destination,
                                   total_amount=ConsignmentAmount(self.qty, self.unloading, self.Frieght, self.total_amount))
                c.save()
                self.company_lg_id = c.id
                fu = FriegthUnloadingLeadger(transaction_type='Debit',description=self.Destination,friegth=self.Frieght*self.qty,unloading=self.unloading*self.qty,total_amount=(self.Frieght*self.qty)+(self.unloading*self.qty) )
                fu.save()
                self.fu_lg_id = fu.id
                warehouse = WareHouseEnventoryLeadger(
                    slug=self.slug, brand=self.brand, qty=self.qty, rate=self.rate, total_amount=self.total_amount, transaction_type='Debit')
                warehouse.save()
                self.wareHouse_lg_id = warehouse.id
        else:
            self.total_amount = (self.qty * self.rate)
            if self.orderStatus == 'Received' and self.company_lg_id == None:
                c = CompanyLeadger(company=self.company, brand=self.brand, qty=self.qty, rate=self.rate,
                                   total_Frieght=self.qty * self.Frieght, total_Unloading=self.qty*self.unloading, transaction_type='Credit',
                                   description=self.Destination,
                                   total_amount=ConsignmentAmount(self.qty, self.unloading, self.Frieght, self.total_amount))
                c.save()
                self.company_lg_id = c.id
                
                fu = FriegthUnloadingLeadger(transaction_type='Debit',description=self.Destination,friegth=self.Frieght*self.qty,unloading=self.unloading*self.qty,
                                             total_amount=(self.Frieght*self.qty)+(self.unloading*self.qty),qty=self.qty )
                fu.save()
                self.fu_lg_id = fu.id
                
                warehouse = WareHouseEnventoryLeadger(
                    slug=self.slug, brand=self.brand, qty=self.qty, rate=self.rate, total_amount=self.total_amount, transaction_type='Debit')
                warehouse.save()
                self.wareHouse_lg_id = warehouse.id
            else:
                # Company Leadger
                c = CompanyLeadger.objects.get(id=self.company_lg_id)
                c.company = self.company
                c.brand = self.brand
                c.qty = self.qty
                c. rate = self.rate
                c.description = self.Destination,
                c.total_Frieght = self.qty * self.Frieght
                c.total_Unloading = self.qty * self.unloading
                c.total_amount = ConsignmentAmount(
                    self.qty, self.unloading, self.Frieght, self.total_amount)
                c.save()
                # FU Leadger
                fu = FriegthUnloadingLeadger.objects.get(id=self.fu_lg_id)
                fu.transaction_type='Debit'
                fu.description=self.Destination
                fu.qty = self.qty
                fu.friegth=self.Frieght*self.qty
                fu.unloading=self.unloading*self.qty
                fu.total_amount=(self.Frieght*self.qty)+(self.unloading*self.qty) 
                fu.save()
                # WareHouse
                warehouse = WareHouseEnventoryLeadger.objects.get(
                    id=self.wareHouse_lg_id)
                warehouse.brand = self.brand
                dispatches = DispatchEnventory.objects.filter(slug=self.slug).values('qty')
                dispatch_qty_sum = 0 
                for i in dispatches:
                    dispatch_qty_sum += i['qty'] 
                
                qty = self.qty 
                qty -= dispatch_qty_sum
                warehouse.qty = qty 
                warehouse.rate = self.rate
                warehouse.total_amount = self.total_amount
                warehouse.save()

        super(OrderPlacement, self).save(*args, **kwargs)

    def __str__(self):
        return self.company.name + ' : ' + self.Destination+' : ' + str(self.
                                                                        date) + '  ( ' + str(self.id) + ' )'


# UI

class DirectCompanyRecieve(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    slug = models.SlugField(null=True, blank=True, default='none5lucky-cement')
    orderStatus = models.CharField(max_length=50, choices=[(
        'Pending', 'Pending'), ('Received', 'Received'), ('Dispatched', 'Dispatched')], default='Pending')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Destination = models.CharField(max_length=50)
    qty = models.IntegerField()
    rate = models.IntegerField()
    FrieghtPerTon = models.FloatField(null=True)
    Frieght_left = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    company_lg_id = models.IntegerField(blank=True, null=True)
    wareHouse_lg_id = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_amount = (self.qty * self.rate)

        if self.id == None:
            code = ''.join(random.choices(
                string.ascii_uppercase + self.company.name, k=10))
            self.slug = slugify(code)
            self.Frieght_left = self.FrieghtPerTon

            if self.orderStatus == 'Received':
                c = CompanyLeadger(company=self.company, brand=self.brand, qty=self.qty, rate=self.rate,
                                   description=self.Destination,
                                   total_Frieght=self.FrieghtPerTon * (self.qty * 50 / 1000), transaction_type='Credit', total_amount=(self.qty * self.rate) - (self.FrieghtPerTon * (self.qty * 50 / 1000)))
                c.save()
                self.company_lg_id = c.id
                warehouse = WareHouseEnventoryLeadger(
                    slug=self.slug, brand=self.brand, qty=self.qty, rate=self.rate, total_amount=self.total_amount, transaction_type='Debit', is_DCR=True)
                warehouse.save()
                self.wareHouse_lg_id = warehouse.id
        else:
            if self.orderStatus == 'Received' and self.company_lg_id == None:
                c = CompanyLeadger(company=self.company, brand=self.brand, qty=self.qty, rate=self.rate,
                                   description=self.Destination,
                                   total_Frieght=self.FrieghtPerTon * (self.qty * 50 / 1000), transaction_type='Credit', total_amount=(self.qty * self.rate) - (self.FrieghtPerTon * (self.qty * 50 / 1000)))
                c.save()
                self.company_lg_id = c.id
                warehouse = WareHouseEnventoryLeadger(
                    slug=self.slug, brand=self.brand, qty=self.qty, rate=self.rate, total_amount=self.total_amount, transaction_type='Debit', is_DCR=True)
                warehouse.save()
                self.wareHouse_lg_id = warehouse.id
            else:
                # Company Leadger
                c = CompanyLeadger.objects.get(id=self.company_lg_id)
                c.company = self.company
                c.brand = self.brand
                c.qty = self.qty
                c.description = self.Destination,
                c. rate = self.rate
                c.total_Frieght = self.FrieghtPerTon * (self.qty * 50 / 1000)
                c.total_amount = (self.qty * self.rate) - \
                    (self.FrieghtPerTon * (self.qty * 50 / 1000))
                c.save()
                # WareHouse
                if self.wareHouse_lg_id:
                    warehouse = WareHouseEnventoryLeadger.objects.get(
                        id=self.wareHouse_lg_id)
                    warehouse.brand = self.brand
                    warehouse.qty = self.qty
                    warehouse.rate = self.rate
                    warehouse.total_amount = self.total_amount
                    warehouse.save()
        super(DirectCompanyRecieve, self).save(*args, **kwargs)

    def __str__(self):
        return self.company.name + ' : ' + self.Destination+' : ' + str(self.
                                                                        date) + '  ( ' + str(self.id) + ' )'

# UI


class PartiesTranspotationManager(models.Model):
    slug = models.SlugField(blank=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    qty = models.IntegerField()
    friegth = models.FloatField(blank=True, default=0)
    unloading = models.FloatField(blank=True, default=0)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    orderPlacement = models.ForeignKey(
        OrderPlacement, on_delete=models.CASCADE, null=True, blank=True)
    directCompanyRecieve = models.ForeignKey(
        DirectCompanyRecieve, on_delete=models.CASCADE, null=True, blank=True)
    fu_lg_id = models.IntegerField(blank=True, null=True)
    driver_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.party}'

    def save(self, *args, **kwargs):
        if self.orderPlacement:
            self.slug = self.orderPlacement.slug
            if self.id == None:
                self.orderPlacement.Frieght_left -= self.friegth
                self.orderPlacement.unloading_left -= self.unloading
                fu = FriegthUnloadingLeadger(party=self.party, transaction_type='Credit', friegth=self.friegth,
                                             unloading=self.unloading, total_amount=(self.qty*self.friegth)+(self.unloading * self.qty), qty=self.qty)
                fu.save()
                self.fu_lg_id = fu.id
                dl = DriverLeadger(driver=self.driver, friegth=self.friegth, unloading=self.unloading, transaction_type='Credit', total_amount=(
                    self.qty*self.friegth)+(self.unloading * self.qty), qty=self.qty)
                dl.save()
                self.driver_lg_id = dl.id
                p = PartyLeadger(party=self.party,qty=self.qty,totalFrieght=self.friegth,totalUnloading=self.unloading,transaction_type='Credit',total_amount=(self.qty*self.friegth)+(self.unloading * self.qty))
                p.save()
                self.party_lg_id = p.id

            self.orderPlacement.save()

        elif self.directCompanyRecieve:
            self.slug = self.directCompanyRecieve.slug
 
            if self.id == None:
                self.directCompanyRecieve.Frieght_left -= self.friegth
            self.directCompanyRecieve.save()
        if self.id != None:
            if self.orderPlacement:
                fu_lg = FriegthUnloadingLeadger.objects.get(id=self.fu_lg_id)
                fu_lg.party = self.party
                fu_lg.qty = self.qty
                fu_lg.friegth = self.friegth
                fu_lg.unloading = self.unloading
                fu_lg.total_amount = (self.qty*self.friegth) + \
                    (self.unloading * self.qty)
                fu_lg.save()
                
                dl = DriverLeadger.objects.get(id=self.driver_lg_id)
                dl.driver = self.driver
                dl.friegth = self.friegth
                dl.unloading = self.unloading
                dl.total_amount = (self.qty*self.friegth) + \
                    (self.unloading * self.qty)
                dl.qty = self.qty
                dl.save()

                p = PartyLeadger.objects.get(id=self.party_lg_id)
                p.party=self.party
                p.qty=self.qty
                p.totalFrieght=self.friegth
                p.totalUnloading=self.unloading
                p.transaction_type='Credit'
                p.total_amount=(self.qty*self.friegth)+(self.unloading * self.qty)
                p.save()

        super(PartiesTranspotationManager, self).save(*args, **kwargs)


# UI


class DispatchEnventory(models.Model):
    party = models.ForeignKey(
        Party, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField()
    qty = models.IntegerField()
    rate = models.FloatField()
    destination = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default='', null=True)
    totalAmount = models.FloatField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)
    warehouse_lg_id = models.IntegerField(blank=True, null=True)
    driver_lg_id = models.IntegerField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        self.totalAmount = (self.qty * self.rate)
        pc = PartiesTranspotationManager.objects.filter(slug=self.slug)
        frieght = 0
        unloading = 0
        qty = 0
        total_frieght = 0
        total_unloading = 0
        for i in pc:
            if self.party == i.party:
                frieght = i.friegth
                unloading = i.unloading
                qty = i.qty
                if i.orderPlacement:
                    total_frieght = qty * frieght
                    total_unloading = qty * unloading
                else:
                    total_frieght = (qty * 50/1000) * frieght
        if self.id == None:
            pl = PartyLeadger(party=self.party, brand=self.brand,
                              qty=self.qty, rate=self.rate, totalFrieght=total_frieght, totalUnloading=total_unloading, transaction_type='Debit',
                              description=self.destination,
                              total_amount=(self.qty * self.rate))
            pl.save()
            self.party_lg_id = pl.id
            
            d = DriverLeadger(driver=self.driver, description=self.destination, transaction_type='Debit',qty=self.qty,friegth=total_frieght,unloading=total_unloading, total_amount=total_frieght+total_unloading )
            d.save()
            self.driver_lg_id = d.id
            
            w = WareHouseEnventoryLeadger.objects.filter(slug=self.slug)[0]
            w.transaction_type = 'Credit'
            if w.is_DCR:
                dc = DirectCompanyRecieve.objects.filter(slug=self.slug)[0]
                dc.orderStatus = 'Dispatched'
                dc.save()
            w.qty -= self.qty
            w.save()
            self.warehouse_lg_id = w.id
        
        else:
            pl = PartyLeadger.objects.get(id=self.party_lg_id)
            pl.brand = self.brand
            pl.qty = self.qty
            pl.rate = self.rate
            pl.description = self.destination,
            pl.total_Frieght = total_frieght
            pl.totalUnloading = total_unloading
            pl.total_amount = (self.qty * self.rate)
            pl.save()

            d = DriverLeadger.objects.get(id=self.driver_lg_id)
            d.driver=self.driver
            d.description=self.destination
            d.transaction_type='Debit'
            d.qty=self.qty
            d.friegth = total_frieght
            d.unloading= total_unloading
            d.total_amount=(self.qty * self.rate) 
            d.save()
        super(DispatchEnventory, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.party)


# UI

class Booking(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    payment_method = models.CharField(
        choices=(('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Bank', 'Bank'), ('Agent', 'Agent'), ('Party', 'Party')), max_length=10)
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, null=True, blank=True)
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, null=True, blank=True)
    amount_paid = models.FloatField()

    company_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    cheque_id = models.IntegerField(blank=True, null=True)
    agent_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            cm = CompanyLeadger(company=self.company, transaction_type='Debit',
                                description=self.payment_method, total_amount=self.amount_paid)
            cm.save()
            self.company_lg_id = cm.id
            if self.payment_method == 'Bank':
                sb = BankLeadger(
                    bank=self.bank, transaction_type='Credit', total_amount=self.amount_paid)
                sb.save()
                self.bank_lg_id = sb.id
            elif self.payment_method == 'Cash':
                cl = CashLeadger(transaction_type='Credit',
                                 description=self.payment_method, total_amount=self.amount_paid)
                cl.save()
                self.cash_lg_id = cl.id
            elif self.payment_method == 'Cheque':
                ch = Cheque(bank=self.bank,
                            description=self.payment_method, transaction_type='Credit', total_amount=self.amount_paid,company=self.company)
                ch.save()
                self.cheque_id = ch.id
            elif self.payment_method == 'Agent':
                ag = AgentLeadger(transaction_type='Credit',
                                  description=self.payment_method, total_amount=self.amount_paid, agent=self.agent)
                ag.save()
                self.agent_lg_id = ag.id
            elif self.payment_method == 'Party':
                pl = PartyLeadger(party=self.party, transaction_type='Credit',
                                  total_amount=self.amount_paid, description=self.payment_method)
                pl.save()
                self.party_lg_id = pl.id
        else:
            cl = CompanyLeadger.objects.get(id=self.company_lg_id)
            cl.agent = self.agent
            cl.company = self.company
            cl.transaction_type = 'Debit'
            cl.description = self.payment_method
            cl.total_amount = self.amount_paid
            cl.save()
            if self.payment_method == 'Bank':
                bl = BankLeadger.objects.get(id=self.bank_lg_id)
                bl.bank = self.bank
                bl.total_amount = self.amount_paid
                bl.save()
            elif self.payment_method == 'Cash':
                cl = CashLeadger.objects.get(id=self.cash_lg_id)
                cl.description = self.payment_method
                cl.total_amount = self.amount_paid
                cl.save()
            elif self.payment_method == 'Cheque':
                ch = Cheque.objects.get(id=self.cheque_id)
                ch.description = self.description
                ch.total_amount = self.recived_amount
                ch.save()
            elif self.payment_method == 'Agent':
                al = AgentLeadger.objects.get(id=self.agent_lg_id)
                al.total_amount = self.amount_paid
                al.agent = self.agent
                al.save()
            elif self.payment_method == 'Party':
                pl = PartyLeadger.objects.get(id=self.party_lg_id)
                pl.party = self.party
                pl.total_amount = self.amount_paid
                pl.save()
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.company.name

# UI


class Recovery(models.Model):
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, blank=True, null=True)
    payment_method = models.CharField(
        choices=(('Cash', 'Cash'), ('Bank', 'Bank'), ('Cheque', 'Cheque')), max_length=10)
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    recived_amount = models.FloatField()
    party_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    agent_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    cheque_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        # Party Leadger
        if self.id == None:
            pl = PartyLeadger(party=self.party, transaction_type='Credit',
                              total_amount=self.recived_amount, description=self.description)
            pl.save()
            self.party_lg_id = pl.id
            if self.payment_method == 'Bank':
                bl = BankLeadger(bank=self.bank, transaction_type='Debit',
                                 total_amount=self.recived_amount, description=self.description)
                bl.save()
                self.bank_lg_id = bl.id
            elif self.payment_method == 'Cash':
                # AgentLeadger
                al = AgentLeadger(transaction_type='Debit',
                                  description=self.description, total_amount=self.recived_amount, agent=self.agent)
                al.save()
                self.agent_lg_id = al.id
            elif self.payment_method == 'Cheque':
                ch = Cheque(party=self.party, bank=self.bank,
                            description=self.description, transaction_type='Debit', total_amount=self.recived_amount)
                ch.save()
                self.cheque_id = ch.id

        else:
            cl = PartyLeadger.objects.get(id=self.party_lg_id)
            cl.party = self.party
            cl.total_amount = self.recived_amount
            cl.description = self.description
            cl.save()
            if self.payment_method == 'Bank':
                bl = BankLeadger.objects.get(id=self.bank_lg_id)
                bl.bank = self.bank
                bl.total_amount = self.recived_amount
                bl.save()
            elif self.payment_method == 'Cash':
                # AgentLeadger
                al = AgentLeadger.objects.get(id=self.agent_lg_id)
                al.total_amount = self.recived_amount
                al.agent = self.agent
                al.description = self.description
                al.save()
                if self.agent.name == static.owner_name:
                    cl = CashLeadger.objects.get(id=self.id)
                    cl.description = self.description
                    cl.total_amount = self.recived_amount
                    cl.save()

                    al = AgentLeadger.objects.get(id=self.agent_ch_lg_id)
                    al.description = self.description
                    al.total_amount = self.recived_amount
                    al.agent = self.agent
                    al.save()
            elif self.payment_method == 'Cheque':
                ch = Cheque.objects.get(id=self.cheque_id)
                ch.party = self.party
                ch.bank = self.bank
                ch.description = self.description
                ch.total_amount = self.recived_amount
                ch.save()

                cl = ChequeLeadger.objects.get(id=ch.cheque_lg_id)
                cl.save()
        super(Recovery, self).save(*args, **kwargs)

    def __str__(self):
        return self.party.name

# Ui


class AgentReceiving(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, default='')
    received_amount = models.FloatField()
    agent_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.agent.name

    def save(self, *args, **kwargs):
        if self.id == None:
            al = AgentLeadger(agent=self.agent, description=self.description,
                              transaction_type='Credit', total_amount=self.received_amount)
            al.save()
            self.agent_lg_id = al.id
            ch = CashLeadger(description=self.description,
                             transaction_type='Debit', total_amount=self.received_amount)
            ch.save()
            self.cash_lg_id = ch.id
        else:
            al = AgentLeadger.objects.get(id=self.agent_lg_id)
            al.total_amount = self.received_amount
            al.agent = self.agent
            al.description = self.description
            al.save()

            cl = CashLeadger.objects.get(id=self.cash_lg_id)
            cl.total_amount = self.received_amount
            cl.description = self.description
            cl.save()

        super(AgentReceiving, self).save(*args, **kwargs)

# Ui


class Expense(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    payment_method = models.CharField(
        choices=(('Cash', 'Cash'), ('Bank', 'Bank'), ('Agent', 'Agent'), ('Party', 'Party')), max_length=10)
    expenseHead = models.ForeignKey(ExpenseHead, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, default='')
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, null=True, blank=True)
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField()
    cash_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    agent_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)
    expense_lg_id = models.IntegerField(blank=True, null=True)

    def __str__(self) -> int:
        return self.expenseHead.name + ' <-Head : Date-> ' + str(self.date)

    def save(self, *args, **kwargs):
        if self.id == None:
            ex = ExpenseLeadger(expenseHead=self.expenseHead,
                                description=self.description, transaction_type='Debit', total_amount=self.amount)
            ex.save()
            self.expense_lg_id = ex.id
            if self.payment_method == 'Bank':
                bl = BankLeadger(bank=self.bank, transaction_type='Credit',
                                 total_amount=self.amount)
                bl.save()
                self.bank_lg_id = bl.id
            elif self.payment_method == 'Cash':
                cl = CashLeadger(
                    transaction_type='Credit', description=self.description, total_amount=self.amount)
                cl.save()
                self.cash_lg_id = cl.id
            elif self.payment_method == 'Agent':
                ag = AgentLeadger(transaction_type='Credit',
                                  description=self.description, total_amount=self.amount, agent=self.agent)
                ag.save()
                self.agent_lg_id = ag.id
            elif self.payment_method == 'Party':
                pl = PartyLeadger(party=self.party, transaction_type='Credit',
                                  total_amount=self.amount, description=self.description)
                pl.save()
                self.party_lg_id = pl.id

        else:
            ex = ExpenseLeadger(id=self.expense_lg_id)
            ex.expenseHead = self.expenseHead
            ex.description = self.description
            ex.total_amount = self.amount
            ex.save()
            if self.payment_method == 'Bank':
                bl = BankLeadger.objects.get(id=self.bank_lg_id)
                bl = self.description
                bl.bank = self.bank
                bl.total_amount = self.amount
                bl.save()
            elif self.payment_method == 'Cash':
                cl = CashLeadger.objects.get(id=self.cash_lg_id)
                cl.description = self.description
                cl.total_amount = self.amount
                cl.save()
            elif self.payment_method == 'Agent':
                ag = AgentLeadger.objects.get(id=self.agent_lg_id)
                ag.description = self.description
                ag.total_amount = self.amount
                ag.agent = self.agent
                ag.save()
            elif self.payment_method == 'Party':
                pl = PartyLeadger.objects.get(id=self.party_lg_id)
                pl.description = self.description
                pl.party = self.party
                pl.total_amount = self.amount
                pl.save()

        super(Expense, self).save(*args, **kwargs)


# UI
# Party Recivings
class PayToParty(models.Model):
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE)
    party_2 = models.ForeignKey(
        Party, on_delete=models.CASCADE, blank=True, null=True, related_name='Part_2')
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, blank=True, null=True)
    payment_method = models.CharField(
        choices=(('Cash', 'Cash'), ('Bank', 'Bank'),('Party', 'Party'), ('Cheque', 'Cheque'), ('Agent','Agent')), max_length=10)
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    recived_amount = models.FloatField()
    party_lg_id = models.IntegerField(blank=True, null=True)
    party2_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    agent_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    cheque_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        # Party Leadger
        if self.id == None:
            pl = PartyLeadger(party=self.party, transaction_type='Debit',
                              total_amount=self.recived_amount, description=self.description)
            pl.save()
            self.party_lg_id = pl.id
            if self.payment_method == 'Bank':
                bl = BankLeadger(bank=self.bank, transaction_type='Credit',
                                 total_amount=self.recived_amount, description=self.description)
                bl.save()
                self.bank_lg_id = bl.id
            elif self.payment_method == 'Agent':
                # AgentLeadger
                al = AgentLeadger(transaction_type='Credit',
                                  description=self.description, total_amount=self.recived_amount, agent=self.agent)
                al.save()
                self.agent_lg_id = al.id
            elif self.payment_method == 'Cash':
                cl = CashLeadger(description=self.description,total_amount=self.recived_amount,transaction_type='Credit')
                cl.save()
                self.cash_lg_id = cl.id
            elif self.payment_method == 'Party':
                pl = PartyLeadger(party=self.party_2, transaction_type='Credit',
                              total_amount=self.recived_amount, description=self.description)
                pl.save()
                self.party2_lg_id = pl.id
            elif self.payment_method == 'Cheque':
                ch = Cheque(party=self.party, bank=self.bank,
                            description=self.description, transaction_type='Credit', total_amount=self.recived_amount)
                ch.save()
                self.cheque_id = ch.id

        else:
            pl = PartyLeadger.objects.get(id=self.party_lg_id)
            pl.party = self.party
            pl.total_amount = self.recived_amount
            pl.description = self.description
            pl.save()
            if self.payment_method == 'Bank':
                bl = BankLeadger.objects.get(id=self.bank_lg_id)
                bl.bank = self.bank
                bl.total_amount = self.recived_amount
                bl.save()
            elif self.payment_method == 'Agent':
                # AgentLeadger
                al = AgentLeadger.objects.get(id=self.agent_lg_id)
                al.total_amount = self.recived_amount
                al.agent = self.agent
                al.description = self.description
                al.save()
            elif self.payment_method == 'Party':
                pl = PartyLeadger.objects.get(party=self.party_2)
                pl.party = self.party_2
                pl.total_amount = self.recived_amount
                pl.description = self.description
                pl.save()
            elif self.payment_method == 'Cheque':
                ch = Cheque.objects.get(id=self.cheque_id)
                ch.party = self.party
                ch.bank = self.bank
                ch.description = self.description
                ch.total_amount = self.recived_amount
                ch.save()
            elif self.payment_method == 'Cash':
                cl = CashLeadger.objects.get(id=self.cash_lg_id)
                cl.description=self.description
                cl.total_amount=self.recived_amount,
                cl.save()
                self.cash_lg_id = cl.id

        super(PayToParty, self).save(*args, **kwargs)

# UI
class PayToBank(models.Model):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE)
    bank_2 = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True, related_name='Bank_2')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE,null=True, blank=True)
    payment_method = models.CharField(
        choices=(('Cash', 'Cash'), ('Bank', 'Bank'),('Party', 'Party'), ('Cheque', 'Cheque'), ('Agent','Agent')), max_length=10)
    description = models.CharField(max_length=50, null=True, blank=True)
    recived_amount = models.FloatField()
    cheque_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    bank2_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)
    agent_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            b = BankLeadger(bank=self.bank, transaction_type='Debit',
                              total_amount=self.recived_amount, description=self.description)
            b.save()
            self.bank_lg_id = b.id
            
            if self.payment_method == 'Bank':
                bl = BankLeadger(bank=self.bank_2, transaction_type='Credit',
                                 total_amount=self.recived_amount, description=self.description)
                bl.save()
                self.bank2_lg_id = bl.id
            
            elif self.payment_method == 'Agent':
                al = AgentLeadger(transaction_type='Credit',
                                  description=self.description, total_amount=self.recived_amount, agent=self.agent)
                al.save()
                self.agent_lg_id = al.id
            
            elif self.payment_method == 'Cash':
                cl = CashLeadger(description=self.description,total_amount=self.recived_amount,transaction_type='Credit')
                cl.save()
                self.cash_lg_id = cl.id
            
            elif self.payment_method == 'Party':
                pl = PartyLeadger(party=self.party, transaction_type='Credit',
                              total_amount=self.recived_amount, description=self.description)
                pl.save()
                self.party_lg_id = pl.id
            
            elif self.payment_method == 'Cheque':
                ch = Cheque(party=self.party, bank=self.bank,
                            description=self.description, transaction_type='Credit', total_amount=self.recived_amount)
                ch.save()
                self.cheque_id = ch.id

        else:
            pl = BankLeadger.objects.get(id=self.bank_lg_id)
            pl.bank = self.bank
            pl.total_amount = self.recived_amount
            pl.description = self.description
            pl.save()
            if self.payment_method == 'Party':
                pl = PartyLeadger.objects.get(id=self.party_lg_id)
                pl.bank = self.bank
                pl.total_amount = self.recived_amount
                pl.save()
            elif self.payment_method == 'Agent':
                # AgentLeadger
                al = AgentLeadger.objects.get(id=self.agent_lg_id)
                al.total_amount = self.recived_amount
                al.agent = self.agent
                al.description = self.description
                al.save()
            elif self.payment_method == 'Bank':
                b = BankLeadger.objects.get(bank=self.bank_2)
                b.bank = self.bank_2
                b.total_amount = self.recived_amount
                b.description = self.description
                b.save()
            elif self.payment_method == 'Cheque':
                ch = Cheque.objects.get(id=self.cheque_id)
                ch.description = self.description
                ch.total_amount = self.recived_amount
                ch.save()
            elif self.payment_method == 'Cash':
                cl = CashLeadger.objects.get(id=self.cash_lg_id)
                cl.description=self.description
                cl.total_amount=self.recived_amount,
                cl.save()

        super(PayToBank, self).save(*args, **kwargs)
    
# UI

class PayToAgent(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    agent_2 = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True,related_name='agent2')
    party = models.ForeignKey(Party, on_delete=models.CASCADE,null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE,null=True, blank=True)
    payment_method = models.CharField(
        choices=(('Cash', 'Cash'), ('Bank', 'Bank'),('Party', 'Party'), ('Cheque', 'Cheque'), ('Agent','Agent')), max_length=10)
    description = models.CharField(max_length=50, null=True, blank=True)
    recived_amount = models.FloatField()
    agent_lg_id = models.IntegerField(blank=True, null=True)
    agent2_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    cheque_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            a = AgentLeadger(agent=self.agent, transaction_type='Debit',
                              total_amount=self.recived_amount, description=self.description)
            a.save()

            self.agent_lg_id = a.id
            
            if self.payment_method == 'Bank':
                bl = BankLeadger(bank=self.bank, transaction_type='Credit',
                                 total_amount=self.recived_amount, description=self.description)
                bl.save()
                self.bank_lg_id = bl.id
            
            elif self.payment_method == 'Agent':
                al = AgentLeadger(transaction_type='Credit',
                                  description=self.description, total_amount=self.recived_amount, agent=self.agent_2)
                al.save()
                self.agent2_lg_id = al.id
            
            elif self.payment_method == 'Cash':
                cl = CashLeadger(description=self.description,total_amount=self.recived_amount,transaction_type='Credit')
                cl.save()
                self.cash_lg_id = cl.id
            
            elif self.payment_method == 'Party':
                pl = PartyLeadger(party=self.party, transaction_type='Credit',
                              total_amount=self.recived_amount, description=self.description)
                pl.save()
                self.party_lg_id = pl.id
            
            elif self.payment_method == 'Cheque':
                ch = Cheque(party=self.party, bank=self.bank,
                            description=self.description, transaction_type='Credit', total_amount=self.recived_amount)
                ch.save()
                self.cheque_id = ch.id

        else:
            al = AgentLeadger.objects.get(id=self.agent_lg_id)
            al.agent = self.agent
            al.total_amount = self.recived_amount
            al.description = self.description
            al.save()

            if self.payment_method == 'Party':
                pl = PartyLeadger.objects.get(id=self.party_lg_id)
                pl.bank = self.bank
                pl.total_amount = self.recived_amount
                pl.save()
            
            elif self.payment_method == 'Agent':
                # AgentLeadger
                al = AgentLeadger.objects.get(id=self.agent2_lg_id)
                al.total_amount = self.recived_amount
                al.agent = self.agent
                al.description = self.description
                al.save()
            elif self.payment_method == 'Bank':
                b = BankLeadger.objects.get(bank=self.bank)
                b.bank = self.bank
                b.total_amount = self.recived_amount
                b.description = self.description
                b.save()
            elif self.payment_method == 'Cheque':
                ch = Cheque.objects.get(id=self.cheque_id)
                ch.party = self.party
                ch.bank = self.bank
                ch.description = self.description
                ch.total_amount = self.recived_amount
                ch.save()
            elif self.payment_method == 'Cash':
                cl = CashLeadger.objects.get(id=self.cash_lg_id)
                cl.description=self.description
                cl.total_amount=self.recived_amount,
                cl.save()

        super(PayToAgent, self).save(*args, **kwargs)


class PayToCashInHandPerson(models.Model):
    cash = models.ForeignKey(CashInHandPerson, on_delete=models.CASCADE)
    payment_method = models.CharField(
        choices=(('Bank', 'Bank'),('Party', 'Party'), ('Agent','Agent')), max_length=10)
    party = models.ForeignKey(Party, on_delete=models.CASCADE,null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE,null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE,null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    recived_amount = models.FloatField()
    agent_lg_id = models.IntegerField(blank=True, null=True)
    bank_lg_id = models.IntegerField(blank=True, null=True)
    party_lg_id = models.IntegerField(blank=True, null=True)
    cash_lg_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            cl = CashLeadger(transaction_type='Debit',
                              total_amount=self.recived_amount, description=self.description)
            cl.save()

            self.cash_lg_id = cl.id
            
            if self.payment_method == 'Bank':
                bl = BankLeadger(bank=self.bank, transaction_type='Credit',
                                 total_amount=self.recived_amount, description=self.description)
                bl.save()
                self.bank_lg_id = bl.id
            
            elif self.payment_method == 'Agent':
                al = AgentLeadger(transaction_type='Credit',
                                  description=self.description, total_amount=self.recived_amount, agent=self.agent)
                al.save()
                self.agent_lg_id = al.id
            
            elif self.payment_method == 'Party':
                pl = PartyLeadger(party=self.party, transaction_type='Credit',
                              total_amount=self.recived_amount, description=self.description)
                pl.save()
                self.party_lg_id = pl.id

        else:
            al = CashLeadger.objects.get(id=self.cash_lg_id)
            al.total_amount = self.recived_amount
            al.description = self.description
            al.save()

            if self.payment_method == 'Party':
                pl = PartyLeadger.objects.get(id=self.party_lg_id)
                pl.bank = self.bank
                pl.total_amount = self.recived_amount
                pl.save()
            
            elif self.payment_method == 'Agent':
                # AgentLeadger
                al = AgentLeadger.objects.get(id=self.agent_lg_id)
                al.total_amount = self.recived_amount
                al.agent = self.agent
                al.description = self.description
                al.save()
            elif self.payment_method == 'Bank':
                b = BankLeadger.objects.get(bank=self.bank)
                b.bank = self.bank
                b.total_amount = self.recived_amount
                b.description = self.description
                b.save()

        super(PayToCashInHandPerson, self).save(*args, **kwargs)

# UI
class ExpectedOrder(models.Model):
    party = models.ForeignKey(Party,on_delete=models.CASCADE)
    expected_orders = models.IntegerField()
    expected_rate = models.FloatField()
    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.party.name