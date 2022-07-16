from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from app.models import *
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    companies = models.ManyToManyField(Company, blank=True)
    parties = models.ManyToManyField(Party, blank=True)
    agents = models.ManyToManyField(Agent, blank=True)
    drivers = models.ManyToManyField(Driver, blank=True)
    cash_in_hps = models.ManyToManyField(CashInHandPerson, blank=True)
    banks = models.ManyToManyField(Bank, blank=True)
    expense_heads = models.ManyToManyField(ExpenseHead, blank=True)
    ui_permissions = models.JSONField(default=dict)
