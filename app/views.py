from django.db.models import Sum
from django.shortcuts import redirect, render, get_object_or_404
from app import serializer as s
from app import models as m
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.http import JsonResponse
from utils import utils


# Create your views here.


class CompanyViewSet(viewsets.ViewSet):

    def list(self, request):
        if request.user.is_superuser:
            company = m.Company.objects.all()
        else:
            company = request.user.companies.all()

        serializer = s.CompanySerializer(
            company, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.CompanySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Company Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Company Data"}

        return JsonResponse(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = s.CompanySerializer(
            company, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = s.CompanySerializer(
                company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.Company.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class AgentsViewSet(viewsets.ViewSet):

    def list(self, request):
        if request.user.is_superuser:
            agent = m.Agent.objects.all()
        else:
            agent = request.user.agents.all()

        serializer = s.AgentSerializer(
            agent, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.AgentSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Company Data"}

        return JsonResponse(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Agent.objects.all()
        agent = get_object_or_404(queryset, pk=pk)
        serializer = s.AgentSerializer(
            agent, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        queryset = m.Agent.objects.all()
        agent = get_object_or_404(queryset, pk=pk)
        serializer = s.AgentSerializer(
            agent, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        dict_response = {"error": False,
                         "message": "Successfully Updated Data"}

        # dict_response = {"error": True,
        #  "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.Agent.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class ExpenseHeadViewSet(viewsets.ViewSet):

    def list(self, request):
        if request.user.is_superuser:
            expenseHead = m.ExpenseHead.objects.all()
        else:
            expenseHead = request.user.agexpense_headsents.all()
        serializer = s.ExpenseHeadSerializer(
            expenseHead, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Expense List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.ExpenseHeadSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Expense Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Expense Data"}

        return JsonResponse(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.ExpenseHead.objects.all()
        expenseHead = get_object_or_404(queryset, pk=pk)
        serializer = s.ExpenseHeadSerializer(
            expenseHead, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.ExpenseHead.objects.all()
            expenseHead = get_object_or_404(queryset, pk=pk)
            serializer = s.ExpenseHeadSerializer(
                expenseHead, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.ExpenseHead.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data "}

        return Response(dict_response)


class PartyViewSet(viewsets.ViewSet):

    def list(self, request):
        if request.user.is_superuser:
            party = m.Party.objects.all()
        else:
            party = request.user.parties.all()

        serializer = s.PartySerializer(
            party, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All party List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.PartySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "party Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving party Data"}

        return JsonResponse(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Party.objects.all()
        party = get_object_or_404(queryset, pk=pk)
        serializer = s.PartySerializer(
            party, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Party.objects.all()
            party = get_object_or_404(queryset, pk=pk)
            serializer = s.PartySerializer(
                party, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.Party.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class BankViewSet(viewsets.ViewSet):

    def list(self, request):
        if request.user.is_superuser():
            bank = m.Bank.objects.all()
        else:
            bank = request.user.banks.all()

        serializer = s.BankSerializer(
            bank, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All party List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.BankSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Bank Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Bank Data"}

        return JsonResponse(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Bank.objects.all()
        bank = get_object_or_404(queryset, pk=pk)
        serializer = s.BankSerializer(
            bank, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Bank.objects.all()
            bank = get_object_or_404(queryset, pk=pk)
            serializer = s.BankSerializer(
                bank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.Bank.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class PartiesTranspotationManagerViewSet(viewsets.ViewSet):

    def list(self, request):
        PartiesCost = m.PartiesTranspotationManager.objects.all()
        serializer = s.PartiesTranspotationManagerSerializer(
            PartiesCost, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All partiesCost List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.PartiesTranspotationManagerSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "PartiesCost Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving PartiesCost Data"}

        return JsonResponse(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.PartiesTranspotationManager.objects.all()
        PartiesCost = get_object_or_404(queryset, pk=pk)
        serializer = s.PartiesTranspotationManagerSerializer(
            PartiesCost, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.PartiesTranspotationManager.objects.all()
            PartiesCost = get_object_or_404(queryset, pk=pk)
            o = m.OrderPlacement.objects.get(slug=PartiesCost.slug)
            # Current value
            c_frieght = o.Frieght_left
            c_unloading = o.unloading_left
            # present value
            p_frieght = PartiesCost.friegth
            p_unloading = PartiesCost.unloading
            # updated value
            u_frieght = p_frieght
            u_unloading = p_unloading

            if 'friegth' in request.data:
                u_frieght = request.data['friegth']
                u_unloading = request.data['unloading']
                u_frieght = int(u_frieght)
                u_unloading = int(u_unloading)
            frieght = p_frieght - u_frieght
            unloading = p_unloading - u_unloading
            frieght = frieght + c_frieght
            unloading = unloading + c_unloading

            serializer = s.PartiesTranspotationManagerSerializer(
                PartiesCost, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.PartiesTranspotationManager.objects.get(id=pk)
            obj.orderPlacement.Frieght_left += obj.friegth * obj.qty
            obj.orderPlacement.unloading_left += obj.unloading * obj.qty
            obj.orderPlacement.save()
            m.PartyLeadger.objects.get(id=obj.party_lg_id).delete()
            m.FriegthUnloadingLeadger.objects.get(id=obj.fu_lg_id).delete()
            m.DriverLeadger.objects.get(id=obj.driver_lg_id).delete()
            obj.delete()

            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class DispatchEnventoryViewSet(viewsets.ViewSet):

    def list(self, request):
        enventory = m.DispatchEnventory.objects.all()
        serializer = s.DispatchEnventorySerializer(
            enventory, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.DispatchEnventorySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            qty = m.WareHouseEnventoryLeadger.objects.get(
                slug=request.POST['slug']).qty
            if (qty - int(request.POST['qty'])) >= 0:
                serializer.save()
                dict_response = {"error": False,
                                 "message": "Company Data Save Successfully"}

            else:
                dict_response = {"error": True,
                                 "message": 'Qunatity Not Avalible. @Avalible qty :' + str(qty)}

        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Company Data"}

        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.DispatchEnventory.objects.all()
        enventory = get_object_or_404(queryset, pk=pk)
        serializer = s.DispatchEnventorySerializer(
            enventory, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.DispatchEnventory.objects.all()
            enventory = get_object_or_404(queryset, pk=pk)
            w = m.WareHouseEnventoryLeadger.objects.get(slug=enventory.slug)
            # Current value
            c_qty = w.qty
            # present value
            p_qt = enventory.qty
            # updated
            u_qty = p_qt
            if 'qty' in request.data:
                u_qty = request.data['qty']
                u_qty = int(u_qty)
            qty = p_qt - u_qty
            qty = qty + c_qty
            w.qty = qty
            w.save()
            serializer = s.DispatchEnventorySerializer(
                enventory, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.DispatchEnventory.objects.get(id=pk)
            m.PartyLeadger.objects.get(id=obj.party_lg_id).delete()
            m.DriverLeadger.objects.get(id=obj.driver_lg_id).delete()
            w = m.WareHouseEnventoryLeadger.objects.get(id=obj.warehouse_lg_id)
            w.qty += obj.qty
            w.save()
            obj.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class OrderPlacementViewSet(viewsets.ViewSet):
    def list(self, request):
        order = m.OrderPlacement.objects.all()
        serializer = s.OrderPlacementSerializer(
            order, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.OrderPlacementSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.OrderPlacement.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = s.OrderPlacementSerializer(
            order, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.OrderPlacement.objects.all()
            order = get_object_or_404(queryset, pk=pk)
            serializer = s.OrderPlacementSerializer(
                order, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.OrderPlacement.objects.get(id=pk)
            if obj.orderStatus == 'Received':
                m.CompanyLeadger.objects.get(id=obj.company_lg_id).delete()
                m.FriegthUnloadingLeadger.objects.get(id=obj.fu_lg_id).delete()
                m.WareHouseEnventoryLeadger.objects.get(
                    id=obj.wareHouse_lg_id).delete()
                # Dispatch Delete
                disp = m.DispatchEnventory.objects.filter(slug=obj.slug)
                for i in disp:
                    m.PartyLeadger.objects.get(id=i.party_lg_id).delete()
                    m.DriverLeadger.objects.get(id=i.driver_lg_id).delete()
                    i.delete()
                # Delete Parties Transpotaions
                pt = m.PartiesTranspotationManager.objects.filter(
                    slug=obj.slug)
                for i in pt:
                    m.PartyLeadger.objects.get(id=i.party_lg_id).delete()
                    m.FriegthUnloadingLeadger.objects.get(
                        id=i.fu_lg_id).delete()
                    m.DriverLeadger.objects.get(id=i.driver_lg_id).delete()

                obj.delete()
            else:
                obj.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class DirectCompanyRecieveViewSet(viewsets.ViewSet):
    def list(self, request):
        order = m.DirectCompanyRecieve.objects.all()
        serializer = s.DirectCompanyRecieveSerializer(
            order, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.DirectCompanyRecieveSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.DirectCompanyRecieve.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = s.DirectCompanyRecieveSerializer(
            order, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.DirectCompanyRecieve.objects.all()
            order = get_object_or_404(queryset, pk=pk)
            serializer = s.DirectCompanyRecieveSerializer(
                order, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.DirectCompanyRecieve.objects.get(id=pk)
            if obj.orderStatus == 'Received':
                m.CompanyLeadger.objects.get(id=obj.company_lg_id).delete()
                w = m.WareHouseEnventoryLeadger.objects.get(
                    id=obj.wareHouse_lg_id).delete()
            obj.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class DriverViewSet(viewsets.ViewSet):
    def list(self, request):
        if request.user.is_superuser:
            driver = m.Driver.objects.all()
        else:
            driver = request.user.drivers.all()

        serializer = s.DriverSerializer(
            driver, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.DriverSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Driver.objects.all()
        driver = get_object_or_404(queryset, pk=pk)
        serializer = s.DriverSerializer(driver, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Driver.objects.all()
            driver = get_object_or_404(queryset, pk=pk)
            serializer = s.DriverSerializer(
                driver, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.Driver.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class BrandViewSet(viewsets.ViewSet):
    def list(self, request):
        brand = m.Brand.objects.all()
        serializer = s.BrandSerializer(
            brand, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.BrandSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Brand.objects.all()
        brand = get_object_or_404(queryset, pk=pk)
        serializer = s.BrandSerializer(brand, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Brand.objects.all()
            brand = get_object_or_404(queryset, pk=pk)
            serializer = s.BrandSerializer(
                brand, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.Brand.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class BookingViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.Booking.objects.all()
        serializer = s.BookingSerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.BookingSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Booking.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        serializer = s.BookingSerializer(
            booking, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Recovery.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.CompanyRecoverySerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.Booking.objects.get(id=pk)
            c = m.CompanyLeadger.objects.get(id=obj.company_lg_id)
            c.delete()
            if obj.payment_method == 'Bank':
                b = m.BankLeadger.objects.get(id=obj.bank_lg_id)
                b.delete()
            elif obj.payment_method == 'Cash':
                c = m.CashLeadger.objects.get(id=obj.cash_lg_id)
                c.delete()
            elif obj.payment_method == 'Cheque':
                m.Cheque.objects.get(id=obj.cheque_id).delete()
            elif obj.payment_method == 'Agent':
                a = m.AgentLeadger.objects.get(id=obj.agent_lg_id)
                a.delete()
            elif obj.payment_method == 'Party':
                p = m.PartyLeadger.objects.get(id=obj.party_lg_id)
                p.delete()
            obj.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class ExpensesViewSet(viewsets.ViewSet):
    def list(self, request):
        expense = m.Expense.objects.all()
        serializer = s.ExpensesSerializer(
            expense, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.ExpensesSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Expense.objects.all()
        expencse = get_object_or_404(queryset, pk=pk)
        serializer = s.ExpensesSerializer(
            expencse, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Expense.objects.all()
            expense = get_object_or_404(queryset, pk=pk)
            serializer = s.ExpensesSerializer(
                expense, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.Expense.objects.get(id=pk)
            m.ExpenseLeadger.objects.get(id=obj.expense_lg_id).delete()
            if obj.payment_method == 'Bank':
                m.BankLeadger.objects.get(id=obj.bank_lg_id).delete()
            elif obj.payment_method == 'Cash':
                m.CashLeadger.objects.get(id=obj.cash_lg_id).delete()
            elif obj.payment_method == 'Agent':
                m.AgentLeadger.objects.get(id=obj.agent_lg_id).delete()
            elif obj.payment_method == 'Party':
                m.PartyLeadger.objects.get(id=obj.party_lg_id).delete()
            obj.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class RecoveryViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.Recovery.objects.all()
        serializer = s.RecoverySerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.RecoverySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.Recovery.objects.all()
        recovery = get_object_or_404(queryset, pk=pk)
        serializer = s.RecoverySerializer(
            recovery, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = m.Recovery.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.RecoverySerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.Recovery.objects.get(id=pk)
            pl = m.PartyLeadger.objects.get(id=obj.party_lg_id)
            if obj.payment_method == 'Bank':
                m.BankLeadger.objects.get(id=obj.bank_lg_id).delete()
            elif obj.payment_method == 'Cash':
                m.AgentLeadger.objects.get(id=obj.agent_lg_id).delete()
            elif obj.payment_method == 'Cheque':
                m.Cheque.objects.get(id=obj.cheque_id).delete()
            pl.delete()
            obj.delete()
            dict_response = {"error": False, "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class PayToPartyViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.PayToParty.objects.all()
        serializer = s.PayToPartySerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.PayToPartySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.PayToParty.objects.all()
        recovery = get_object_or_404(queryset, pk=pk)
        serializer = s.PayToPartySerializer(
            recovery, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            print(request)
            queryset = m.PayToParty.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.PayToPartySerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.PayToParty.objects.get(id=pk)
            pl = m.PartyLeadger.objects.get(id=obj.party_lg_id)

            if obj.payment_method == 'Agent':
                m.AgentLeadger.objects.get(id=obj.agent_lg_id).delete()
            elif obj.payment_method == 'Bank':
                m.BankLeadger.objects.get(id=obj.bank_lg_id).delete()
            elif obj.payment_method == 'Cash':
                m.CashLeadger.objects.get(id=obj.cash_lg_id).delete()
            elif obj.payment_method == 'Cheque':
                cq = m.Cheque.objects.get(id=obj.cheque_id)
                c = m.ChequeLeadger.objects.get(id=cq.cheque_lg_id)
                c.delete()
                cq.delete()
            elif obj.payment_method == 'Party':
                p2l = m.PartyLeadger.objects.get(id=obj.party2_lg_id)
                p2l.delete()

            pl.delete()
            obj.delete()
            dict_response = {"error": False, "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class PayToBankViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.PayToBank.objects.all()
        serializer = s.PayToBankSerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.PayToBankSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.PayToBank.objects.all()
        recovery = get_object_or_404(queryset, pk=pk)
        serializer = s.PayToBankSerializer(
            recovery, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            print(request)
            queryset = m.PayToBank.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.PayToBankSerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.PayToBank.objects.get(id=pk)
            bl = m.BankLeadger.objects.get(id=obj.bank_lg_id)
            if obj.payment_method == 'Bank':
                m.BankLeadger.objects.get(id=obj.bank2_lg_id).delete()
            elif obj.payment_method == 'Cash':
                m.CashLeadger.objects.get(id=obj.cash_lg_id).delete()
            elif obj.payment_method == 'Cheque':
                m.Cheque.objects.get(id=obj.cheque_id).delete()
            elif obj.payment_method == 'Party':
                m.PartyLeadger.objects.get(id=obj.party_lg_id).delete()
            elif obj.payment_method == 'Agent':
                m.AgentLeadger.objects.get(id=obj.agent_lg_id).delete()
            bl.delete()

            obj.delete()
            dict_response = {"error": False, "message": "Successfully Deleted"}

        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class PayToAgentViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.PayToAgent.objects.all()
        serializer = s.PayToAgentSerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.PayToAgentSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.PayToAgent.objects.all()
        recovery = get_object_or_404(queryset, pk=pk)
        serializer = s.PayToAgentSerializer(
            recovery, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            print(request)
            queryset = m.PayToAgent.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.PayToAgentSerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.PayToAgent.objects.get(id=pk)
            m.AgentLeadger.objects.get(id=obj.agent_lg_id).delete()
            if obj.payment_method == 'Bank':
                m.BankLeadger.objects.get(id=obj.bank_lg_id).delete()
            elif obj.payment_method == 'Cash':
                m.CashLeadger.objects.get(id=obj.cash_lg_id).delete()
            elif obj.payment_method == 'Cheque':
                m.Cheque.objects.get(id=obj.cheque_id).delete()
            elif obj.payment_method == 'Party':
                m.PartyLeadger.objects.get(id=obj.party_lg_id).delete()
            elif obj.payment_method == 'Agent':
                m.AgentLeadger.objects.get(id=obj.agent2_lg_id).delete()
            obj.delete()
            dict_response = {"error": False, "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class PayToCashInHandPersonViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.PayToCashInHandPerson.objects.all()
        serializer = s.PayToCashInHandPersonSerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.PayToCashInHandPersonSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.PayToCashInHandPerson.objects.all()
        recovery = get_object_or_404(queryset, pk=pk)
        serializer = s.PayToCashInHandPersonSerializer(
            recovery, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            print(request)
            queryset = m.PayToCashInHandPerson.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.PayToCashInHandPersonSerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            obj = m.PayToCashInHandPerson.objects.get(id=pk)
            m.CashLeadger.objects.get(id=obj.cash_lg_id).delete()
            if obj.payment_method == 'Bank':
                m.BankLeadger.objects.get(id=obj.bank_lg_id).delete()
            elif obj.payment_method == 'Party':
                m.PartyLeadger.objects.get(id=obj.party_lg_id).delete()
            elif obj.payment_method == 'Agent':
                m.AgentLeadger.objects.get(id=obj.agent_lg_id).delete()
            obj.delete()
            dict_response = {"error": False, "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class ExpectedOrderViewSet(viewsets.ViewSet):
    def list(self, request):
        recovery = m.ExpectedOrder.objects.all()
        serializer = s.ExpectedOrderSerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = s.ExpectedOrderSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = m.ExpectedOrder.objects.all()
        recovery = get_object_or_404(queryset, pk=pk)
        serializer = s.ExpectedOrderSerializer(
            recovery, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            print(request)
            queryset = m.ExpectedOrder.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.ExpectedOrderSerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Updating Data"}

        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            m.ExpectedOrder.objects.get(id=pk).delete()
            dict_response = {"error": False, "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class WareHouseDiplayViewSet(viewsets.ViewSet):

    def list(self, request):
        recovery = m.WareHouseEnventoryLeadger.objects.all()
        serializer = s.WareHouseEnventoryLeadgerSerializer(
            recovery, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def delete(self, request, pk=None):
        try:
            m.WareHouseEnventoryLeadger.objects.get(id=pk).delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}

        return Response(dict_response)


class WareHouseWithSulg(generics.ListAPIView):
    serializer_class = s.WareHouseEnventoryLeadgerSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return m.WareHouseEnventoryLeadger.objects.filter(slug=slug)


class Recivings(viewsets.ViewSet):
    def list(self, request):
        receiving = m.AgentReceiving.objects.all()
        serializer = s.ReceivingSerializer(
            receiving, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = m.AgentReceiving.objects.all()
        receiving = get_object_or_404(queryset, pk=pk)
        serializer = s.ReceivingSerializer(
            receiving, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def create(self, request):
        try:
            serializer = s.ReceivingSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            ar = m.AgentReceiving.objects.get(id=pk)
            a = m.AgentLeadger(id=ar.agent_lg_id)
            a.delete()
            cl = m.CashLeadger(id=ar.cash_lg_id)
            cl.delete()
            ar.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)


class DriverReceiving(viewsets.ViewSet):
    def list(self, request):
        receiving = m.DriverReceiving.objects.all()
        serializer = s.DriverReceivingSerializer(
            receiving, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = m.DriverReceiving.objects.all()
        receiving = get_object_or_404(queryset, pk=pk)
        serializer = s.DriverReceivingSerializer(
            receiving, context={"request": request})
        serializer_data = serializer.data
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def create(self, request):
        try:
            serializer = s.DriverReceivingSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Data Save Successfully"}
        except ValueError as err:
            dict_response = {"error": True, "message": err}
        except:
            dict_response = {"error": True,
                             "message": "Error During Saving Data"}
        return Response(dict_response)

    def delete(self, request, pk=None):
        try:
            d = m.DriverReceiving.objects.get(id=pk)
            m.FriegthUnloadingLeadger.objects.get(id=d.fu_lg_id).delete()
            m.DriverLeadger.objects.get(id=d.driver_lg_id).delete()

            d.delete()
            dict_response = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            dict_response = {"error": True,
                             "message": "Error During Deleted Data Data"}
        return Response(dict_response)

# Oprations


def orderStatusupdate(request, pk):
    try:
        order = m.OrderPlacement.objects.get(id=pk)
        order.orderStatus = 'Received'
        order.save()
        dict_response = {'error': False,
                         'mesaage': 'Order Status Sccuessfuly update and Ware House Enventory Added'
                         }
    except:
        dict_response = {'error': True,
                         'mesaage': 'Order Status not update due to some Errors'
                         }
    return JsonResponse(dict_response)


def CompanyRecieveStatusupdate(request, pk):
    try:

        order = m.DirectCompanyRecieve.objects.get(id=pk)
        order.orderStatus = 'Received'
        order.save()
        dict_response = {'error': False,
                         'mesaage': 'CompanyRecieve Status Sccuessfuly update and Ware House Enventory Added'
                         }
    except:
        dict_response = {'error': True,
                         'mesaage': 'CompanyRecieve Status not update due to some Errors'
                         }
    return JsonResponse(dict_response)


def ChequeStatusupdate(request, pk, status):
    try:
        ch = m.ChequeLeadger.objects.get(id=pk)
        ch.chequeStatus = status
        ch.save()

        dict_response = {'error': False,
                         'mesaage': 'Cheque Status Sccuessfuly update and Ware House Enventory Added'
                         }
    except:
        dict_response = {'error': True,
                         'mesaage': 'Cheque Status not update due to some Errors'
                         }
    return JsonResponse(dict_response)


def test(request):
    companyLg = m.CompanyLeadger.objects.all()
    partyLg = m.PartyLeadger.objects.all()
    agentLg = m.AgentLeadger.objects.all()
    cashLg = m.CashLeadger.objects.all()
    bankLg = m.BankLeadger.objects.all()
    expenceLg = m.ExpenseLeadger.objects.all()
    chequeLg = m.ChequeLeadger.objects.all()
    f_u = m.FriegthUnloadingLeadger.objects.all()
    driver = m.DriverLeadger.objects.all()
    # utils.ExpenseTest()
    context = {
        'companyLg': companyLg,
        'partLg': partyLg,
        'agentLg': agentLg,
        'cashLg':  cashLg,
        'bankLg': bankLg,
        'Expense': expenceLg,
        'Cheque': chequeLg,
        'FU': f_u,
        'Driver': driver,
    }
    return render(request, 'app/test.html', context=context)


def AddEntities(request):
    # utils.AddAgent()
    # utils.AddDriver()
    # utils.AddCashPerson()
    # utils.AddCashFlowPerson()
    # utils.AddCompany()
    # utils.Bank()
    # utils.Brand()
    # utils.AddExpenseHead()
    # utils.AddParties()
    # utils.OrderPlace_Transporation()
    # utils.Recovery()
    # utils.Booking()
    # for dispatch in m.DispatchEnventory.objects.all():
    #     pty = m.PartyLeadger.objects.get(id=dispatch.party_lg_id)
    #     dispatch.date = pty.date
    #     dispatch.save()
    return redirect('/app/test')
# Leadgers Views


class BankLeadgerView(generics.ListAPIView):
    queryset = m.BankLeadger.objects.all()
    serializer_class = s.BankLeadgerSerializer


class PartyLeadgerView(generics.ListAPIView):
    queryset = m.PartyLeadger.objects.all()
    serializer_class = s.PartyLeadgerSerializer


class CashLeadgerView(generics.ListAPIView):
    queryset = m.CashLeadger.objects.all()
    serializer_class = s.CashLeadgerSerializer


class ChequeLeadgerView(generics.ListAPIView):
    queryset = m.ChequeLeadger.objects.all()
    serializer_class = s.ChequeLeadgerSerializer


class AgentLeadgerView(generics.ListAPIView):
    queryset = m.AgentLeadger.objects.all()
    serializer_class = s.AgentLeadgerSerializer


class CompanyLeadgerView(generics.ListAPIView):
    queryset = m.CompanyLeadger.objects.all()
    serializer_class = s.CompanyLeadgerSerializer


class ExpenseLeadgerView(generics.ListAPIView):
    queryset = m.ExpenseLeadger.objects.all()
    serializer_class = s.ExpenceLeadgerSerializer


class DriverLeadgerView(generics.ListAPIView):
    queryset = m.DriverLeadger.objects.all()
    serializer_class = s.DriverLeadgerSerializer


class FrieghtUnloadingLeadgerView(generics.ListAPIView):
    queryset = m.FriegthUnloadingLeadger.objects.all()
    serializer_class = s.FriegthUnloadingLeadgerSerializer


# Filter Leadgers

class CompanyLeadgerFilter(generics.ListAPIView):
    serializer_class = s.CompanyLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        company = self.kwargs['company']
        return m.CompanyLeadger.objects.filter(company=company, date__lte=t_date, date__gte=f_date)


class AgentLeadgerFilter(generics.ListAPIView):
    serializer_class = s.AgentLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        agent = self.kwargs['agent']
        return m.AgentLeadger.objects.filter(agent=agent, date__lte=t_date, date__gte=f_date)


class BankLeadgerFilter(generics.ListAPIView):
    serializer_class = s.BankLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        bank = self.kwargs['bank']
        return m.BankLeadger.objects.filter(bank=bank, date__lte=t_date, date__gte=f_date)


class ExpenceLeadgerFilter(generics.ListAPIView):
    serializer_class = s.ExpenceLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        head = self.kwargs['expenceHead']
        return m.ExpenseLeadger.objects.filter(expenseHead=head, date__lte=t_date, date__gte=f_date)


class DriverLeadgerFilter(generics.ListAPIView):
    serializer_class = s.DriverLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        driver = self.kwargs['driver']
        return m.DriverLeadger.objects.filter(driver=driver, date__lte=t_date, date__gte=f_date)


class FrieghtUnloadingLeadgerFilter(generics.ListAPIView):
    serializer_class = s.FriegthUnloadingLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        party = self.kwargs['party']
        return m.FriegthUnloadingLeadger.objects.filter(party=party, date__lte=t_date, date__gte=f_date)


class PartyLeadgerFilter(generics.ListAPIView):
    serializer_class = s.PartyLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        party = self.kwargs['party']
        return m.PartyLeadger.objects.filter(party=party, date__lte=t_date, date__gte=f_date)


class CashLeadgerFilter(generics.ListAPIView):
    serializer_class = s.CashLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.CashLeadger.objects.filter(date__lte=t_date, date__gte=f_date)


class ChequeLeadgerFilter(generics.ListAPIView):
    serializer_class = s.ChequeLeadgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.ChequeLeadger.objects.filter(date__lte=t_date, date__gte=f_date)


class ChequeFilter(generics.ListAPIView):
    serializer_class = s.ChequeSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.Cheque.objects.filter(date__lte=t_date, date__gte=f_date)


# Filter Obj
class ChequeFilter(generics.ListAPIView):
    serializer_class = s.ChequeSerializer
    queryset = m.Cheque.objects.all()


class CashInHandPersonFilter(generics.ListAPIView):
    serializer_class = s.CashInHandPersonSerializer
    queryset = m.CashInHandPerson.objects.all()


class BookingFilter(generics.ListAPIView):
    serializer_class = s.BookingSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.Booking.objects.filter(date__lte=t_date, date__gte=f_date)


class DispatchEnventoryFilter(generics.ListAPIView):
    serializer_class = s.DispatchEnventorySerializer
    queryset = serializer_class.data

    def get_queryset(self):
        slug = self.kwargs['slug']
        return m.DispatchEnventory.objects.filter(slug=slug)


class OrderPlacementFilter(generics.ListAPIView):
    serializer_class = s.OrderPlacementSerializer
    queryset = serializer_class.data

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.OrderPlacement.objects.filter(date__lte=t_date, date__gte=f_date)


class BookingFilter(generics.ListAPIView):
    serializer_class = s.BookingSerializer
    queryset = m.Booking.objects.all()

    def get_queryset(self):
        date = self.kwargs['date']
        return m.Booking.objects.filter(date=date)


class RecoveryFilter(generics.ListAPIView):
    serializer_class = s.RecoverySerializer
    queryset = m.Recovery.objects.all()

    def get_queryset(self):
        date = self.kwargs['date']
        return m.Recovery.objects.filter(date=date)


class DirectCompanyDispatchFilter(generics.ListAPIView):
    serializer_class = s.DirectCompanyRecieveSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.DirectCompanyRecieve.objects.filter(date__lte=t_date, date__gte=f_date)


class PartiesTranspotationsFilter(generics.ListAPIView):
    serializer_class = s.PartiesTranspotationManagerSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return m.PartiesTranspotationManager.objects.filter(slug=slug)

# Queries filtring


def FilterPartyList(request, FromDate, ToDate):
    try:
        query = m.PartyLeadger.objects.filter(date__lte=ToDate, date__gte=FromDate, brand__isnull=False).values(
            'party__name', 'brand__name').annotate(brandSum=Sum('qty'))

        parties = set()
        for party in query:
            parties.add(party['party__name'])

        result = {}
        for p in parties:
            result[p] = [i for i in query.filter(
                party__name=p).values('brand__name', 'brandSum')]

        for i in result:
            nt = m.PartyLeadger.objects.filter(date__lte=ToDate, date__gte=FromDate).filter(
                party__name=i).values('net_Balancse').last()
            result[i].append(nt)

        re = []
        for key, value in result.items():
            nt = value[-1]
            value.pop()
            re.append([{'Name': key}, value, nt])

        response = {'error': False, 'data': re}
    except:
        response = {'error': True, 'data': 'Error in data'}

    # return JsonResponse(response,safe=False)
    # try:
    #     c = m.PartyLeadger.objects.filter(date__lte=ToDate, date__gte=FromDate).filter(brand__isnull=False).values('brand').annotate(brand_qty_sum=Sum('qty')).values('brand_qty_sum','party__name','brand__name','net_Balancse').order_by('date')
    #     data = []
    #     if len(c):
    #         for i in c:
    #             data.append({'productName':i['party__name'],'brandName':i['brand__name'],'brandQtySum':i['brand_qty_sum'],'net_Balancse:':i['net_Balancse']})

    #     response = {'error':False,'data': data}
    # except:
    #         response = {'error':True,'data':'Error in data'}

    return JsonResponse(response, safe=False)


def FilterPartyNetBalance(request, date):
    query = m.PartyLeadger.objects.filter(date__lte=date)
    res = []
    parties = {}

    for i in query:
        response = {}
        if i.party.name in parties:
            parties[i.party.name] = i.net_Balancse
        else:
            parties[i.party.name] = 0.0
    res.append(parties)

    return JsonResponse(res, safe=False)


def FilterExpectedOrder(request, FromDate, ToDate):
    query = m.ExpectedOrder.objects.filter(date__lte=ToDate, date__gte=FromDate).values(
        'party').annotate(expected_orders=Sum('expected_orders'), expected_rate=Sum('expected_rate'))
    res = []
    for i in query:
        i['party'] = m.Party.objects.get(id=i['party']).name
        res.append(i)
    # party = m.Party.objects.get(name=name)
    # res = []
    # query = m.ExpectedOrder.objects.filter(party=party,date__gte=FromDate,date__lte=ToDate).values('id','party','expected_orders','expected_rate','date')
    # for i in query:
    #     i['party'] = m.Party.objects.get(id=i['party']).name
    #     res.append(i)
    return JsonResponse(res, safe=False)

# Trial Balance


def TrialBalanceCalculate(request):
    companies = m.CompanyLeadger.objects.values(
        'company__name', 'transaction_type').annotate(total=Sum('total_amount'))
    parties = m.PartyLeadger.objects.values(
        'party__name', 'transaction_type').annotate(total=Sum('total_amount'))
    agents = m.AgentLeadger.objects.values(
        'agent__name', 'transaction_type').annotate(total=Sum('total_amount'))
    driver = m.DriverLeadger.objects.values(
        'driver__name', 'transaction_type').annotate(total=Sum('total_amount'))
    banks = m.BankLeadger.objects.values(
        'bank__name', 'transaction_type').annotate(total=Sum('total_amount'))
    cash = m.CashLeadger.objects.values(
        'cashInHandPerson__name', 'transaction_type').annotate(total=Sum('total_amount'))
    cheques = m.ChequeLeadger.objects.values(
        'transaction_type').annotate(total=Sum('total_amount'))
    expences = m.ExpenseLeadger.objects.values(
        'expenseHead__name', 'transaction_type').annotate(total=Sum('total_amount'))
    Fu = m.FriegthUnloadingLeadger.objects.values(
        'cashFlow__name', 'transaction_type').annotate(total=Sum('total_amount'))

    result = []
    # Companies
    creadit_total = 0
    debit_total = 0
    for i in companies:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    companies = {'Account Payables': creadit_total - debit_total}
    # Parties
    creadit_total = 0
    debit_total = 0
    for i in parties:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    parties = {'Account Recievables': debit_total - creadit_total}
    # agents
    creadit_total = 0
    debit_total = 0
    for i in agents:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    agents = {'Cash In Hand Persons': debit_total - creadit_total}
    # driver
    creadit_total = 0
    debit_total = 0
    for i in driver:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    driver = {'Drivers': debit_total - creadit_total}
    # banks
    creadit_total = 0
    debit_total = 0
    for i in banks:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    banks = {'Banks': debit_total - creadit_total}
    # cash
    creadit_total = 0
    debit_total = 0
    for i in cash:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    cash = {'Cash': debit_total - creadit_total}
    # cheques
    creadit_total = 0
    debit_total = 0
    for i in cheques:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    cheques = {'cheques': debit_total - creadit_total}
    # expences
    expences = [i for i in expences]
    # Fu
    creadit_total = 0
    debit_total = 0
    for i in Fu:
        if i['transaction_type'] == 'Credit':
            creadit_total += i['total']
        else:
            debit_total += i['total']
    Fu = {'FU': debit_total - creadit_total}

    result.append(companies)
    result.append(parties)
    result.append(agents)
    result.append(banks)
    result.append(driver)
    result.append(cash)
    result.append(cheques)
    result.append(expences)
    result.append(Fu)

    return JsonResponse(result, safe=False)


def DispatchReport(request):
    dispatches = m.DispatchEnventory.objects.all()

    list = []
    for dispatch in dispatches:
        w = m.WareHouseEnventoryLeadger.objects.first()
        dict = {'date': dispatch.date, 'PartyName': dispatch.party.name, 'Brand': dispatch.brand.name, 'qty': dispatch.qty,
                'Sales Rate': dispatch.rate, "Amount": dispatch.rate * dispatch.qty, 'Purchaserate': w.rate, "Profit Amount": ((dispatch.rate * dispatch.qty) - (dispatch.qty * w.rate))}
        list.append(dict)

    return JsonResponse(list, safe=False)
