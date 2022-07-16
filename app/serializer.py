
from django.db import models
from django.db.models import fields
from . import models as m
from rest_framework import serializers as s


class CompanySerializer(s.ModelSerializer):
    class Meta:
        model = m.Company
        fields = '__all__'


class BrandSerializer(s.ModelSerializer):
    class Meta:
        model = m.Brand
        fields = '__all__'


class BankSerializer(s.ModelSerializer):
    class Meta:
        model = m.Bank
        fields = '__all__'


class CashInHandPersonSerializer(s.ModelSerializer):
    class Meta:
        model = m.CashInHandPerson
        fields = '__all__'


class ExpenseHeadSerializer(s.ModelSerializer):
    class Meta:
        model = m.ExpenseHead
        fields = '__all__'


class AgentSerializer(s.ModelSerializer):
    class Meta:
        model = m.Agent
        fields = '__all__'


class PartySerializer(s.ModelSerializer):
    class Meta:
        model = m.Party
        fields = '__all__'


class DriverSerializer(s.ModelSerializer):
    class Meta:
        model = m.Driver
        fields = '__all__'


class WareHouseEnventoryLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.WareHouseEnventoryLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class OrderPlacementSerializer(s.ModelSerializer):
    class Meta:
        model = m.OrderPlacement
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        response['driver'] = DriverSerializer(instance.driver).data
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class DirectCompanyRecieveSerializer(s.ModelSerializer):
    class Meta:
        model = m.DirectCompanyRecieve
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class PartiesTranspotationManagerSerializer(s.ModelSerializer):
    class Meta:
        model = m.PartiesTranspotationManager
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        return response


class DispatchEnventorySerializer(s.ModelSerializer):
    class Meta:
        model = m.DispatchEnventory
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        response['driver'] = DriverSerializer(instance.driver).data
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class BookingSerializer(s.ModelSerializer):

    class Meta:
        model = m.Booking
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        response['bank'] = BankSerializer(instance.bank).data
        response['party'] = PartySerializer(instance.party).data
        response['agent'] = AgentSerializer(instance.agent).data
        return response


class RecoverySerializer(s.ModelSerializer):
    class Meta:
        model = m.Recovery
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        response['bank'] = BankSerializer(instance.bank).data
        response['agent'] = AgentSerializer(instance.agent).data
        return response


class PayToPartySerializer(s.ModelSerializer):
    class Meta:
        model = m.PayToParty
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        response['party_2'] = PartySerializer(instance.party_2).data
        response['bank'] = BankSerializer(instance.bank).data
        response['agent'] = AgentSerializer(instance.agent).data
        return response


class PayToBankSerializer(s.ModelSerializer):
    class Meta:
        model = m.PayToBank
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bank'] = BankSerializer(instance.bank).data
        response['bank_2'] = BankSerializer(instance.bank_2).data
        response['party'] = PartySerializer(instance.party).data
        response['agent'] = AgentSerializer(instance.agent).data
        return response

class PayToAgentSerializer(s.ModelSerializer):
    class Meta:
        model = m.PayToAgent
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bank'] = BankSerializer(instance.bank).data
        response['agent'] = AgentSerializer(instance.agent).data
        response['agent_2'] = AgentSerializer(instance.agent_2).data
        response['party'] = PartySerializer(instance.party).data
        return response

class PayToCashInHandPersonSerializer(s.ModelSerializer):
    class Meta:
        model = m.PayToCashInHandPerson
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bank'] = BankSerializer(instance.bank).data
        response['agent'] = AgentSerializer(instance.agent).data
        response['party'] = PartySerializer(instance.party).data
        return response


class ReceivingSerializer(s.ModelSerializer):
    class Meta:
        model = m.Recovery
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['agent'] = AgentSerializer(instance.agent).data
        return response


class DriverReceivingSerializer(s.ModelSerializer):

    class Meta:
        model = m.DriverReceiving
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['driver'] = DriverSerializer(instance.driver).data
        return response


class ExpensesSerializer(s.ModelSerializer):
    class Meta:
        model = m.Expense
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bank'] = BankSerializer(instance.bank).data
        response['expenseHead'] = ExpenseHeadSerializer(
            instance.expenseHead).data
        response['agent'] = AgentSerializer(instance.agent).data
        return response


class FriegthUnloadingLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.FriegthUnloadingLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        return response


class ChequeSerializer(s.ModelSerializer):
    
    class Meta:
        model = m.Cheque
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        response['bank'] = BankSerializer(instance.bank).data
        response['cheque_lg_id'] = ChequeLeadgerSerializer(m.ChequeLeadger.objects.get(id=instance.cheque_lg_id)).data
        return response
# Leadgers Serializers


class CompanyLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.CompanyLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class BankLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.BankLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bank'] = BankSerializer(instance.bank).data
        return response


class CashLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.CashLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cashInHandPerson'] = CashInHandPersonSerializer(
            instance.cashInHandPerson).data
        return response


class PartyLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.PartyLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class AgentLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.AgentLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['agent'] = AgentSerializer(instance.agent).data
        return response


class ExpenceLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.ExpenseLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['expenseHead'] = ExpenseHeadSerializer(
            instance.expenseHead).data
        return response


class DriverLeadgerSerializer(s.ModelSerializer):
    class Meta:
        model = m.DriverLeadger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['driver'] = DriverSerializer(instance.driver).data
        return response


class ChequeLeadgerSerializer(s.ModelSerializer):

    class Meta:
        model = m.ChequeLeadger
        fields = '__all__'


class ExpectedOrderSerializer(s.ModelSerializer):

    class Meta:
        model = m.ExpectedOrder
        fields = '__all__'
