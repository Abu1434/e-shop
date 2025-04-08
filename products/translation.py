from modeltranslation.translator import register, TranslationOptions

from products.models import CategoryModel, ColorModel, BannerModel, ProductModel


@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ColorModel)
class ColorModelTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(BannerModel)
class BannerModelTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ("name", "short_description", "long_description", )
