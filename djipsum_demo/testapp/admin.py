from __future__ import absolute_import

from django.contrib import admin
from testapp.models import TestField


class TestFieldAdmin(admin.ModelAdmin):
    list_display = ['test_CharField', 'test_BooleanField', 'test_DateTimeField', 'test_EmailField']
    list_filter = ['test_BooleanField', 'test_NullBooleanField', 'test_DateField']
    search_fields = ['test_CharField', 'test_EmailField']
    list_per_page = 20

admin.site.register(TestField, TestFieldAdmin)
