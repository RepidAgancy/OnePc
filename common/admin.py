from django.contrib import admin
from django.contrib.auth.models import Group

from common import models

admin.site.unregister(Group)


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Video', {"fields": ('video',)}),
        ('Uzbek tilida', ({'fields': ("title_uz", 'description_uz')})),
        ('Rus tilida', ({'fields': ("title_ru", "description_ru")})),
        ('Ingliz tilida', ({'fields': ("title_en", "description_en")})),
    ]
    list_display = ['title',]
    list_display_links = list_display


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['link', 'image_uz', 'image_ru', 'image_en']
    list_display_links = list_display


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_contacted']
    list_display_links = list_display
    list_filter = ['is_contacted']
