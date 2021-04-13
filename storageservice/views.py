from django.shortcuts import render
from rest_framework import views
from rest_framework import response
from rest_framework import generics
from .models import Entity
from .serializers import Serializer
from django.db.models import F, Sum


class MainView(generics.ListCreateAPIView, generics.GenericAPIView):
    queryset = Entity.objects.all()
    serializer_class = Serializer

class DetailView(generics.RetrieveAPIView,generics.UpdateAPIView, generics.DestroyAPIView,generics.GenericAPIView):
    lookup_field = 'id'
    queryset = Entity.objects.all()
    serializer_class = Serializer

class TotalCost(views.APIView):
    def get(self, request):
        # calculate total_cost
        cost = Entity.objects.values("price", "amount").annotate(sum=F("price") * F("amount")).aggregate(
            total_cost=Sum("sum"))
        return response.Response(cost)
