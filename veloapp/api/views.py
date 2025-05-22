from django.shortcuts import render
from rest_framework import generics
from .models import Hit
from .serializers import HitSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class HitListCreateView(generics.ListCreateAPIView):
    queryset = Hit.objects.all().order_by('-created_at')[:20]
    serializer_class = HitSerializer

class HitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HitSerializer
    lookup_field = 'title_url'

    def get_queryset(self):
        return Hit.objects.all()