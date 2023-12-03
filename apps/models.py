from django.db.models import Model, CharField, DateTimeField, SET_NULL, ImageField, DecimalField, IntegerField, \
    ForeignKey, CASCADE , BooleanField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from parler.models import TranslatableModel


# Create your models here.
class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(MPTTModel):
    name = CharField(max_length=25)
    parent = TreeForeignKey('self', SET_NULL, related_name='category', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=255)
    description = CharField(max_length=1500)
    image = ImageField(upload_to='images/', null=True, blank=True)
    price = DecimalField(max_digits=9, decimal_places=2)
    amount = IntegerField(default=1)
    is_sale = BooleanField(default=False)
    sale_price = DecimalField(default=0, max_digits=9, decimal_places=2)
    category = ForeignKey(Category, CASCADE, related_name='product', null=True, blank=True)

    def __str__(self):
        return self.name
