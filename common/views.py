from django.shortcuts import render

from rest_framework import generics, permissions, response, status

from common import models, serializers


class AboutUsApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.AboutUsSerializer
    queryset = models.AboutUs.objects.all()


class AdvertisementApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.AdvertisementSerializer
    queryset = models.Adversitement.objects.all()


class DiscountAdvertisementApiView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.AdvertisementSerializer
    queryset = models.DiscountAdvertisement.objects.all()


class ContactUsApiView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ContactUsSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            data = serializer.save()
            return response.Response(data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



