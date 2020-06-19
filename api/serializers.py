from rest_framework import serializers

from api.models import Salaries


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = ["name", "position", "department", "salary"] #avoids asking for ID while posting
    