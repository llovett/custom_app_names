from django.contrib import admin
from exampleapp.models import Foo, Bar

class ExampleAdmin(admin.ModelAdmin):
    verbose_name = "Custom Title"

class FooAdmin(ExampleAdmin):
    pass

class BarAdmin(ExampleAdmin):
    pass

admin.site.register(Foo, FooAdmin)
admin.site.register(Bar, BarAdmin)
