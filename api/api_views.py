from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from api.models import Salaries
from api.serializers import SalariesSerializer


class SalariesAPIView(CreateModelMixin, GenericAPIView):
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
