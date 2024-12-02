from modeltranslation.translator import TranslationOptions, register

from product import models


@register(models.ProductComponents)
class AboutUsTranslation(TranslationOptions):
    fields = ['info_name', 'info_text']