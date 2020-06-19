from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response

from api.models import Salaries
from api.serializers import SalariesSerializer


class SalariesAPIView(CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer

    def get(self, request, *args, **kwargs):
        name = self.request.GET.get('name', None)
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        queryset = self.paginate_queryset(queryset=self.queryset)
        serializer = SalariesSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        obj_id = self.request.GET.get('id', None)
        instance = Salaries.objects.get(id=obj_id)
        serializer = SalariesSerializer(instance, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
