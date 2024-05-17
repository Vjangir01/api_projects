from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import flight_details
from .serilizers import FlightDetailsSer

# Create your views here.
class Flight(APIView):
    def get(self,r):
        flightdetails = flight_details.objects.all()
        serobj = FlightDetailsSer(flightdetails,many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj = FlightDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class flightUpdateDelete(APIView):
    def put(self,r,pk):
        flightobj = flight_details.objects.get(pk=pk) # data from database
        serobj = FlightDetailsSer(flightobj,data=r.data) # data from client
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,r,pk):
        fligtobj = flight_details.objects.get(pk=pk)
        fligtobj.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)




