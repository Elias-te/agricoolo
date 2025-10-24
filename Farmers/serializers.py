from rest_framework import serializers
from .models import AnalysisRequest

class AnalysisRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisRequest
        fields = "__all__"
