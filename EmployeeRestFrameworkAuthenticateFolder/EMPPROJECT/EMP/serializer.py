from rest_framework import serializers
from .models import EmpModel

class EmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmpModel
        fields = "__all__"