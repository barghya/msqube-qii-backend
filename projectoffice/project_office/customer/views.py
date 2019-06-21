from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from customer.serializers import TblAddressSerializer, TblCommChannelSerializer, TblCustomerSerializer, TblCustomerAditionalAttributeSerializer, TblEmailSerializer, TblLegalInfoSerializer, TblPhoneSerializer, TblProjectSerializer, TblProjectAttributesSerializer
from customer.models import TblAddress, TblCommChannel, TblCustomer, TblCustomerAditionalAttribute, TblEmail, TblLegalInfo, TblPhone, TblProject, TblProjectAttributes


class TblAddressAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblAddress.objects.get(pk=id)
            serializer = TblAddressSerializer(item)
            return Response(serializer.data)
        except TblAddress.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblAddress.objects.get(pk=id)
        except TblAddress.DoesNotExist:
            return Response(status=404)
        serializer = TblAddressSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblAddress.objects.get(pk=id)
        except TblAddress.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblAddressAPIListView(APIView):

    def get(self, request, format=None):
        items = TblAddress.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblAddressSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblCommChannelAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblCommChannel.objects.get(pk=id)
            serializer = TblCommChannelSerializer(item)
            return Response(serializer.data)
        except TblCommChannel.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblCommChannel.objects.get(pk=id)
        except TblCommChannel.DoesNotExist:
            return Response(status=404)
        serializer = TblCommChannelSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblCommChannel.objects.get(pk=id)
        except TblCommChannel.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblCommChannelAPIListView(APIView):

    def get(self, request, format=None):
        items = TblCommChannel.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblCommChannelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblCommChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblCustomerAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblCustomer.objects.get(pk=id)
            serializer = TblCustomerSerializer(item)
            return Response(serializer.data)
        except TblCustomer.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblCustomer.objects.get(pk=id)
        except TblCustomer.DoesNotExist:
            return Response(status=404)
        serializer = TblCustomerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblCustomer.objects.get(pk=id)
        except TblCustomer.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblCustomerAPIListView(APIView):

    def get(self, request, format=None):
        items = TblCustomer.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblCustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblCustomerAditionalAttributeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblCustomerAditionalAttribute.objects.get(pk=id)
            serializer = TblCustomerAditionalAttributeSerializer(item)
            return Response(serializer.data)
        except TblCustomerAditionalAttribute.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblCustomerAditionalAttribute.objects.get(pk=id)
        except TblCustomerAditionalAttribute.DoesNotExist:
            return Response(status=404)
        serializer = TblCustomerAditionalAttributeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblCustomerAditionalAttribute.objects.get(pk=id)
        except TblCustomerAditionalAttribute.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblCustomerAditionalAttributeAPIListView(APIView):

    def get(self, request, format=None):
        items = TblCustomerAditionalAttribute.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblCustomerAditionalAttributeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblCustomerAditionalAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblEmailAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblEmail.objects.get(pk=id)
            serializer = TblEmailSerializer(item)
            return Response(serializer.data)
        except TblEmail.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblEmail.objects.get(pk=id)
        except TblEmail.DoesNotExist:
            return Response(status=404)
        serializer = TblEmailSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblEmail.objects.get(pk=id)
        except TblEmail.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblEmailAPIListView(APIView):

    def get(self, request, format=None):
        items = TblEmail.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblEmailSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblLegalInfoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblLegalInfo.objects.get(pk=id)
            serializer = TblLegalInfoSerializer(item)
            return Response(serializer.data)
        except TblLegalInfo.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblLegalInfo.objects.get(pk=id)
        except TblLegalInfo.DoesNotExist:
            return Response(status=404)
        serializer = TblLegalInfoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblLegalInfo.objects.get(pk=id)
        except TblLegalInfo.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblLegalInfoAPIListView(APIView):

    def get(self, request, format=None):
        items = TblLegalInfo.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblLegalInfoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblLegalInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblPhoneAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblPhone.objects.get(pk=id)
            serializer = TblPhoneSerializer(item)
            return Response(serializer.data)
        except TblPhone.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblPhone.objects.get(pk=id)
        except TblPhone.DoesNotExist:
            return Response(status=404)
        serializer = TblPhoneSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblPhone.objects.get(pk=id)
        except TblPhone.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblPhoneAPIListView(APIView):

    def get(self, request, format=None):
        items = TblPhone.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblPhoneSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblPhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblProjectAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblProject.objects.get(pk=id)
            serializer = TblProjectSerializer(item)
            return Response(serializer.data)
        except TblProject.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblProject.objects.get(pk=id)
        except TblProject.DoesNotExist:
            return Response(status=404)
        serializer = TblProjectSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblProject.objects.get(pk=id)
        except TblProject.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblProjectAPIListView(APIView):

    def get(self, request, format=None):
        items = TblProject.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblProjectSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TblProjectAttributesAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TblProjectAttributes.objects.get(pk=id)
            serializer = TblProjectAttributesSerializer(item)
            return Response(serializer.data)
        except TblProjectAttributes.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TblProjectAttributes.objects.get(pk=id)
        except TblProjectAttributes.DoesNotExist:
            return Response(status=404)
        serializer = TblProjectAttributesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TblProjectAttributes.objects.get(pk=id)
        except TblProjectAttributes.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TblProjectAttributesAPIListView(APIView):

    def get(self, request, format=None):
        items = TblProjectAttributes.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TblProjectAttributesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TblProjectAttributesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
