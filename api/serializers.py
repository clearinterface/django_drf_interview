from rest_framework import serializers

from api.models import Salaries


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = '__all__'