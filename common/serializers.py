from rest_framework import serializers

from common.models import AboutUs, Adversitement, ContactUs, DiscountAdvertisement


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            'uuid', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en', 'video'
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
            'uuid', 'image_uz', 'image_en', 'image_ru', 
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