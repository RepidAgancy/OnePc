from modeltranslation.translator import TranslationOptions, register

from common.models import AboutUs, Adversitement

@register(AboutUs)
class AboutUsModelTranslation(TranslationOptions):
    fields = ('title', 'description' )


@register(Adversitement)
class AdvertisementModelTranslation(TranslationOptions):
    fields = ('image', )