from __future__ import absolute_import

from django.contrib import admin
from testapp.models import TestFaker, TestField


class TestFakerAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created', 'publish']
    list_filter = ['created', 'publish']
    search_fields = ['title', 'user__username', 'description']
    list_per_page = 20


class TestFieldAdmin(admin.ModelAdmin):
    list_display = ['test_CharField', 'test_BooleanField', 'test_DateTimeField', 'test_EmailField']
    list_filter = ['test_BooleanField', 'test_NullBooleanField', 'test_DateField']
    search_fields = ['test_CharField', 'test_EmailField']
    list_per_page = 20


admin.site.register(TestFaker, TestFakerAdmin)
admin.site.register(TestField, TestFieldAdmin)
