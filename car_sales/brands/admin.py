from django.contrib import admin
from brands.models import Brands

# Register your models here.

class brandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("brand_name", )}
    list_display = ["brand_name", "slug"]

admin.site.register(Brands, brandAdmin)