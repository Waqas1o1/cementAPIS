from django.contrib.auth import models
import os
from app import models as m


def ConsignmentAmount(qty, unloading, freight, totalAmount):
    totalUnloading = qty * unloading
    totalFreight = qty * freight
    return totalAmount - (totalFreight + totalUnloading)


def updateCurrentBalance(type, last):
    if type == 'Cash':
        last.cashInHandPerson.current_Balance = last.net_Balancse
        last.cashInHandPerson.save()
    elif type == 'Bank':
        last.bank.current_Balance = last.net_Balancse
        last.bank.save()
    elif type == 'Company':
        last.company.current_Balance = last.net_Balancse
        last.company.save()
    elif type == 'Party':
        last.party.current_Balance = last.net_Balancse
        last.party.save()
    elif type == 'Agent':
        last.agent.current_Balance = last.net_Balancse
        last.agent.save()
    elif type == 'FU':
        last.cashFlow.current_Balance = last.net_Balancse
        last.cashFlow.save()
    elif type == 'Expense':
        last.expenseHead.current_Balance = last.net_Balancse
        last.expenseHead.save()
    elif type == 'Driver':
        last.driver.current_Balance = last.net_Balancse
        last.driver.save()
    elif type == 'Cheque':
        c = m.CheckCashFlow.objects.first()
        c.current_Balance = last.net_Balancse
        c.save()


def updateCurrentBalanceToOpeniing(type, last):
    if type == 'Cash':
        last.cashInHandPerson.current_Balance = last.cashInHandPerson.opening_Balance
        last.cashInHandPerson.save()
    elif type == 'Bank':
        last.bank.current_Balance = last.bank.opening_Balance
        last.bank.save()
    elif type == 'Company':
        last.company.current_Balance = last.company.opening_Balance
        last.company.save()
    elif type == 'Party':
        last.party.current_Balance = last.party.opening_Balance
        last.party.save()
    elif type == 'Agent':
        last.agent.current_Balance = last.agent.opening_Balance
        last.agent.save()
    elif type == 'FU':
        last.cashFlow.current_Balance = last.cashFlow.opening_Balance
        last.cashFlow.save()
    elif type == 'Expense':
        last.expenseHead.current_Balance = last.expenseHead.opening_Balance
        last.expenseHead.save()
    elif type == 'Driver':
        last.driver.current_Balance = last.driver.opening_Balance
        last.driver.save()
    elif type == 'Cheque':
        c = m.CheckCashFlow.objects.first()
        c.current_Balance = last.opening_Balance
        c.save()


def GetReliventLeadger(type, l, obj):
    if type == 'Cash':
        l = l.filter(cashInHandPerson=obj.cashInHandPerson)
    elif type == 'Bank':
        l = l.filter(bank=obj.bank)
    elif type == 'Company':
        l = l.filter(company=obj.company)
    elif type == 'Party':
        l = l.filter(party=obj.party)
    elif type == 'Agent':
        l = l.filter(agent=obj.agent)
    elif type == 'Expense':
        l = l.filter(expenseHead=obj.expenseHead)
    elif type == 'FU':
        l = l.filter(cashFlow=obj.cashFlow)
    elif type == 'Driver':
        l = l.filter(driver=obj.driver)
    elif type == 'Cheque':
        l = m.CheckCashFlow.objects.first()
    return l


def UpdateLeadgers(obj, leadger, type, isReverse=False):
    l = leadger.objects.all()

    l = GetReliventLeadger(type, l, obj)

    l = l.filter(id__gte=obj.id).order_by('id')

    try:
        obj.total_amount = obj.total_amount[0]
        diff = obj.total_amount - l.first().total_amount
    except TypeError:
        diff = obj.total_amount - l.first().total_amount

    last = obj

    for i in l:
        if obj.transaction_type == 'Credit':
            if isReverse:
                i.net_Balancse -= diff
            else:
                i.net_Balancse += diff

        else:
            if isReverse:
                i.net_Balancse += diff
            else:
                i.net_Balancse -= diff

        i.save(updating=True)
        if i == l.last():
            last = i

    updateCurrentBalance(type, last)

    return l.first()


def DeleteLeadgers(obj, leadger, type, isReverse=False):
    l = leadger.objects.all()

    l = GetReliventLeadger(type, l, obj)

    l = l.filter(id__gte=obj.id).order_by('id')

    last = obj

    if len(l) == 1:
        updateCurrentBalanceToOpeniing(type, last)
    else:
        for i in l[1:]:
            if obj.transaction_type == 'Credit':
                if isReverse:
                    i.net_Balancse += obj.total_amount
                else:
                    i.net_Balancse -= obj.total_amount
                i.save(updating=True)
            else:
                if isReverse:
                    i.net_Balancse -= obj.total_amount
                else:
                    i.net_Balancse += obj.total_amount
                i.save(updating=True)
            if i == l.last():
                last = i
        updateCurrentBalance(type, last)

    obj.delete(updating=True)


def ExpenseTest():
    m.ExpenseLeadger.objects.all().delete()
    eh = m.CashInHandPerson.objects.all().first()
    eh.current_Balance = 0
    eh.opening_Balance = 0
    eh.save()
    m.Expense.objects.all().delete()
    m.CashLeadger.objects.all().delete()
    h = m.ExpenseHead.objects.first()
    for i in range(100, 600, 100):
        ex = m.Expense(payment_method='Cash', expenseHead=h, amount=i)
        ex.save()


def AddParties():
    for a in m.Party.objects.all():
        a.delete()
    jb = m.Party(name='Jabbar Traders Mianwali',
                 opening_Balance=0, contact='03122012330')
    jb.save()
    nh = m.Party(name='Naveed Hardware Multan',
                 opening_Balance=0, contact='03122012330')
    nh.save()
    kh = m.Party(name='Khan Brothers bhawalpure',
                 opening_Balance=0, contact='03122012330')
    kh.save()


def AddExpenseHead():
    for a in m.ExpenseHead.objects.all():
        a.delete()
    cf = m.ExpenseHead(name='Car Fuel', opening_Balance=0)
    cf.save()
    mb = m.ExpenseHead(name='Mobile Bill', opening_Balance=0)
    mb.save()
    r = m.ExpenseHead(name='Rent', opening_Balance=0)
    r.save()
    b = m.ExpenseHead(name='Bill', opening_Balance=0)
    b.save()


def Brand():
    m.Brand.objects.all().delete()
    m.Brand(name='Lucky Cement').save()


def AddCompany():
    m.Company.objects.all().delete()
    lc = m.Company(name='Lucky Cement Pvt LTD',
                   opening_Balance=0, contact='03127073731')
    lc.save()
    ml = m.Company(name='Maple Leaf Cement Pvt Ltd',
                   opening_Balance=0, contact='03127073731')
    ml.save()


def AddDriver():
    m.Driver.objects.all().delete()
    ll = m.Driver(name='lala main Shai ALi',
                  vihical_no='SLK 4689', contact='03127073731', opening_Balance=0)
    ll.save()


def AddCashPerson():
    m.CashInHandPerson.objects.all().delete()
    cp = m.CashInHandPerson(name='Moazam', opening_Balance=0)
    cp.save()


def AddCashFlowPerson():
    m.CheckCashFlow.objects.all().delete()
    mo = m.CheckCashFlow(name='Moazam', opening_Balance=0)
    mo.save()
    m.FUCashFLow.objects.all().delete()
    mo = m.FUCashFLow(name='FuCashFlow', opening_Balance=0)
    mo.save()


def AddAgent():
    m.Agent.objects.all().delete()
    w = m.Agent(name='Waqas',
                opening_Balance=0, contact='03127073731')
    w.save()
    t = m.Agent(name='Badar',
                opening_Balance=0, contact='03127073731')
    t.save()
    t = m.Agent(name='Moazam',
                opening_Balance=0, contact='03127073731')
    t.save()


def Bank():
    for b in m.Bank.objects.all():
        b.delete()
    b = m.Bank(name='HBL Boson Road', account=0,
               contact='03127073731', address='xyz', opening_Balance=0)
    b.save()
    b = m.Bank(name='Al Habib', account=0,
               contact='03127073731', address='xyz', opening_Balance=0)
    b.save()


# Tables
def OrderPlace_Transporation():
    b = m.Brand.objects.get(name='Lucky Cement')
    m.OrderPlacement.objects.all().delete()
    c = m.Company.objects.get(name='Lucky Cement Pvt LTD')
    d = m.Driver.objects.get(name='lala main Shai ALi')
    o = m.OrderPlacement(company=c, driver=d, qty=500,
                         rate=535, Frieght=11, unloading=12, brand=b, orderStatus='Received')
    o.save()
    jb = m.Party.objects.get(name='Jabbar Traders Mianwali')
    m.PartiesTranspotationManager.objects.all().delete()
    pt1 = m.PartiesTranspotationManager(
        party=jb, qty=500, friegth=15, orderPlacement=o)
    pt1.save()
    nv = m.Party.objects.get(name='Naveed Hardware Multan')
    pt2 = m.PartiesTranspotationManager(
        party=nv, qty=500, unloading=15, orderPlacement=o)
    # Dispatched
    pt2.save()
    b = m.Brand.objects.get(name='Lucky Cement')
    dj = m.DispatchEnventory(party=jb, qty=300, rate=550,
                             brand=b, destination='FSD', vehical='SLK', slug=o.slug)
    dj.save()
    d = m.DispatchEnventory(party=nv, qty=200, rate=550,
                            brand=b, destination='FSD', vehical='SLK', slug=o.slug)
    d.save()


def Recovery():
    jb = m.Party.objects.get(name='Jabbar Traders Mianwali')
    nv = m.Party.objects.get(name='Naveed Hardware Multan')
    a = m.Agent.objects.get(name='Badar')
    w = m.Agent.objects.get(name='Waqas')
    r = m.Recovery(party=jb, agent=a, payment_method='Cash',
                   description='Easy Passa', recived_amount=50000)
    r.save()
    r = m.Recovery(party=nv, agent=w, payment_method='Cash',
                   description='Easy Passa', recived_amount=20000)
    r.save()


def Booking():
    c = m.Company.objects.get(name='Lucky Cement Pvt LTD')
    a = m.Agent.objects.get(name='Badar')
    b = m.Booking(company=c, agent=a,
                  payment_method='Agent', amount_paid=20000)
    b.save()
