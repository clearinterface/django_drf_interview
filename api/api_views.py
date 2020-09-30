from rest_framework.generics import GenericAPIView
from api.models import Salaries
from rest_framework import serializers, status
from rest_framework.response import Response
from api.serializers import SalariesSerializer


class SalariesAPIView(GenericAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(queryset=self.queryset)
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = self.paginate_queryset(queryset=self.queryset.filter(name__icontains=name))
        serializer = SalariesSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        salary = Salaries.objects.create(**request.data)

        serializer = SalariesSerializer(instance=salary, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params.get("id")

        try:
            salary = Salaries.objects.get(id=id)
            for k,v in request.data.items():
                setattr(salary, k, v)
            salary.save()
            serializer = SalariesSerializer(instance=salary, context={'request': request})
            return Response(serializer.data)
        except Salaries.DoesNotExist:
            salary = Salaries.objects.create(**request.data)

            serializer = SalariesSerializer(instance=salary, context={'request': request})
            return Response(serializer.data)



  


