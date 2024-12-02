from rest_framework import serializers

from common.models import AboutUs, Adversitement, ContactUs, DiscountAdvertisement


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            'uuid', 'title', 'description', 'video'
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adversitement
        fields = (
            'uuid', 'image', 'link'
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountAdvertisement
        fields = (
            'uuid', 'image', 
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'name', 'phone_number'
        )

    def create(self, validated_data):
        form = ContactUs.objects.create(
            name = validated_data['name'],
            phone_number = validated_data['phone_number']
        )
        return {
            'message':"Form created successfully"
        }