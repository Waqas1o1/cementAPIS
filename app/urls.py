from django.urls import path, include
from app import views
from rest_framework import routers




router = routers.DefaultRouter()
router.register("company", views.CompanyViewSet, basename="company")
router.register("agent", views.AgentsViewSet, basename="agent")
router.register("wareHouse", views.WareHouseDiplayViewSet,
                basename="wareHouse")
router.register("party", views.PartyViewSet, basename="party")
router.register("expenseHead", views.ExpenseHeadViewSet,
                basename="expenseHead")
router.register("bank", views.BankViewSet, basename="bank")
router.register("orderPlacement", views.OrderPlacementViewSet,
                basename="orderPlacement")
router.register("PartiesTranspotationManagerViewSet",
                views.PartiesTranspotationManagerViewSet, basename="PartiesTranspotationManagerViewSet")
router.register("directCompanyRecieve", views.DirectCompanyRecieveViewSet,
                basename="directCompanyRecieve")
router.register("dispatchEnventory",
                views.DispatchEnventoryViewSet, basename='dispatchEnventory')
router.register("driver", views.DriverViewSet, basename="driver")
router.register("brand", views.BrandViewSet, basename="brand")
router.register("Booking", views.BookingViewSet,
                basename="Booking")
router.register("Expenses", views.ExpensesViewSet, basename="Expenses")
router.register("Recovery", views.RecoveryViewSet,
                basename="Recovery")
router.register("PayToParty", views.PayToPartyViewSet,
                basename="PayToParty")
router.register("PayToBank", views.PayToBankViewSet,
                basename="PayToBank")
router.register("PayToAgent", views.PayToAgentViewSet,
                basename="PayToAgent")
router.register("PayToCashInHandPerson", views.PayToCashInHandPersonViewSet,
                basename="PayToCashInHandPerson")
router.register("DriverReceiving", views.DriverReceiving,
                basename="driverReceiving")
router.register("AgentReceivings", views.Recivings, basename='AgentReceivings')
router.register("ExpectedOrder", views.ExpectedOrderViewSet, basename='ExpectedOrder')


urlpatterns = [
    path('', include(router.urls)),
    # Leadgers
    path('BankLeadger', views.BankLeadgerView.as_view(), name='bankleagder'),
    path('AgentLeadger', views.AgentLeadgerView.as_view(), name='agentleagder'),
    path('PartyLeadger', views.PartyLeadgerView.as_view(), name='partyleagder'),
    path('CompanyLeadger', views.CompanyLeadgerView.as_view(), name='companyleagder'),
    path('CashLeadger', views.CashLeadgerView.as_view(), name='cashleagder'),
    path('ChequeLeadger', views.ChequeLeadgerView.as_view(), name='chequeleagder'),
    path('ExpenseLeadger', views.ExpenseLeadgerView.as_view(), name='expenseleagder'),
    path('FULeadger', views.FrieghtUnloadingLeadgerView.as_view(), name='fUleagder'),
    path('DriverLeadger', views.DriverLeadgerView.as_view(), name='driverleadger'),

    # Oprations
    path('getwareHouse/<slug:slug>', views.WareHouseWithSulg.as_view()),
    path('orderStatusupdate/<int:pk>', views.orderStatusupdate),
    path('chequeStatusupdate/<int:pk>/<str:status>', views.ChequeStatusupdate),
    path('CompanyRecieveStatusupdate/<int:pk>',
         views.CompanyRecieveStatusupdate),
    path('test', views.test),
    path('AddEntities', views.AddEntities),
    #     Filter
    path('FilterorderPlacement/<str:FromDate>/<str:ToDate>',
         views.OrderPlacementFilter.as_view()),
    path('FilterdispatchEnventory/<slug:slug>',
         views.DispatchEnventoryFilter.as_view()),
    path('FilterBooking/<str:FromDate>/<str:ToDate>',
         views.BookingFilter.as_view()),
    path('FilterDirectCompanyDispatch/<str:FromDate>/<str:ToDate>',
         views.DirectCompanyDispatchFilter.as_view()),
    path('Charge_FU/<slug:slug>', views.PartiesTranspotationsFilter.as_view()),
    path('CashInHandPerson/', views.CashInHandPersonFilter.as_view()),
    path('ChequeFilter/<str:FromDate>/<str:ToDate>',views.ChequeFilter.as_view()),
    path('GetPartiesNetBalance/<str:ToDate>',views.GetPartiesNetBalance),

    # Get Leadgers By date
    path('FilterCompanyLeadger/<str:FromDate>/<str:ToDate>/<int:company>',
         views.CompanyLeadgerFilter.as_view()),
    path('FilterBankLeadger/<str:FromDate>/<str:ToDate>/<int:bank>',
         views.BankLeadgerFilter.as_view()),
    path('FilterPartyLeadger/<str:FromDate>/<str:ToDate>/<int:party>',
         views.PartyLeadgerFilter.as_view()),
    path('FilterChequeLeadger/<str:FromDate>/<str:ToDate>',
         views.ChequeLeadgerFilter.as_view()),
    path('FilterCashLeadger/<str:FromDate>/<str:ToDate>',
         views.CashLeadgerFilter.as_view()),
    path('FilterAgentLeadger/<str:FromDate>/<str:ToDate>/<int:agent>',
         views.AgentLeadgerFilter.as_view()),
    path('FilterExpenceLeadger/<str:FromDate>/<str:ToDate>/<str:expenceHead>',
         views.ExpenceLeadgerFilter.as_view()),
    path('FilterFrieghtUnloadingLeadger/<str:FromDate>/<str:ToDate>/<int:party>',
         views.FrieghtUnloadingLeadgerFilter.as_view()),
    path('FilterDriverLeadger/<str:FromDate>/<str:ToDate>/<int:driver>',
         views.DriverLeadgerFilter.as_view()),
    path('BookingFilter/<str:date>',views.BookingFilter.as_view()),
    path('RecoveryFilter/<str:date>',views.RecoveryFilter.as_view()),
    path('ChequeFilter/', views.ChequeFilter.as_view()),

     #Queries 
     path('FilterParty/<str:FromDate>/<str:ToDate>', views.FilterPartyList),
     path('FilterPartyNetBalance/<str:date>', views.FilterPartyNetBalance),
     path('FilterExpectedOrder/<str:FromDate>/<str:ToDate>', views.FilterExpectedOrder),
     # TrialBalanceCalculate
     path('TrialBalanceCalculate/', views.TrialBalanceCalculate),
     # Backup ANd Restore
     path('RorB-Data/', views.Backup_or_RestoreData),

     # Dispatch
     path('DispacthReport/<str:FromDate>/<str:ToDate>', views.DispatchReport),
     path('CheckRestoreFiles/', views.CheckRestoreFiles),
     # PDF
     path('PartyLedgerPDF/<int:party>/<str:FromDate>/<str:ToDate>', views.GenratePartyLedgerPDF.as_view()),
     path('CompanyLedgerPDF/<int:company>/<str:FromDate>/<str:ToDate>', views.GenrateCompanyLedgerPDF.as_view()),
     path('AgentLedgerPDF/<int:agent>/<str:FromDate>/<str:ToDate>', views.GenrateAgentLedgerPDF.as_view()),
     path('DriverLedgerPDF/<int:driver>/<str:FromDate>/<str:ToDate>', views.GenrateDriverLedgerPDF.as_view()),
     path('ExpenceLedgerPDF/<int:expenseHead>/<str:FromDate>/<str:ToDate>', views.GenrateExpenceLedgerPDF.as_view()),
     path('BankLedgerPDF/<int:bank>/<str:FromDate>/<str:ToDate>', views.GenrateBankLedgerPDF.as_view()),
     path('CashLedgerPDF/<str:FromDate>/<str:ToDate>', views.GenrateCashLedgerPDF.as_view()),
     path('ChequeLedgerPDF/<str:FromDate>/<str:ToDate>', views.GenrateChequeLedgerPDF.as_view()),
     path('FULedgerPDF/<int:party>/<str:FromDate>/<str:ToDate>', views.GenrateFULedgerPDF.as_view()),
     path('DispatchReportPDF/<str:FromDate>/<str:ToDate>', views.GenrateDispatchReportPDF.as_view()),
     
]
