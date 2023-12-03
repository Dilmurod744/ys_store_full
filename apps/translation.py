from modeltranslation.translator import TranslationOptions, register

from apps.models import Category, Product


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ['name', ]


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ['name', 'description', ]
