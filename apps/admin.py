from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'description', 'image_show', 'price']

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(ProductAdmin, self).get_queryset(request)

        #     return super(ProductAdmin, self).get_queryset(request)
        else:
            qs = super(ProductAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='150' />".format(obj.image.url))

        return 'None'

    image_show.__name__ = 'images'


class CategoryAdmin(TranslationAdmin):
    list_display = ['name', ]
