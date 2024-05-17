from rest_framework import serializers
from .models import flight_details

class FlightDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = flight_details
        fields = "__all__"

