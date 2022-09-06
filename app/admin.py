from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register((OrderPlacement, Brand, Party,
                     CompanyLeadger, Company, Driver, Booking, Agent, Recovery, DispatchEnventory, AgentLeadger, PartyLeadger, WareHouseEnventoryLeadger, Bank, BankLeadger, CashLeadger, DirectCompanyRecieve, AgentReceiving, CashInHandPerson, Expense, ExpenseHead, ExpenseLeadger, PartiesTranspotationManager))
admin.site.register((ChequeLeadger, CheckCashFlow,ExpectedOrder,
                     Cheque, FriegthUnloadingLeadger, FUCashFLow, DriverReceiving,PayToParty,PayToBank,PayToAgent,PayToCashInHandPerson))
admin.site.site_header = "Real Services Development"
# admin.site.site_title = ""
# admin.site.index_title = ""
