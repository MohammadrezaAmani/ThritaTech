from rest_framework import serializers
from .models import Session
from prescription.serializers import PrescriptionSerializer

class SessionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Session model.
    """
    prescription = PrescriptionSerializer(many=True)  # Assuming you have a PrescriptionSerializer

    class Meta:
        model = Session
        fields = "__all__"
    

class SessionSerializerRate(serializers.ModelSerializer):
    """
    Serializer for the Session model.
    """
    class Meta:
        model = Session
        fields = ['rate']