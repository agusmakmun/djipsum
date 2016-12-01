from __future__ import absolute_import

import uuid
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class TestField(models.Model):
    # test_AutoField = models.AutoField()
    # test_BigAutoField = models.BigAutoField()
    test_BigIntegerField = models.BigIntegerField()
    test_BinaryField = models.BinaryField()
    test_BooleanField = models.BooleanField()
    test_CharField = models.CharField(max_length=200)

    # CommaSeparatedIntegerField has been deprecated. Support for it (except in historical migrations) will be removed in Django 2.0.
    # HINT: Use CharField(validators=[validate_comma_separated_integer_list]) instead.
    #test_CommaSeparatedIntegerField = models.CommaSeparatedIntegerField(max_length=200)

    test_DateField = models.DateField(auto_now_add=True)
    test_DateTimeField = models.DateTimeField(auto_now_add=True)
    test_DecimalField = models.DecimalField(max_digits=19, decimal_places=2, default=19.0)
    test_DurationField = models.DurationField(default=datetime.timedelta(days=1))
    test_EmailField = models.EmailField()
    test_FileField = models.FileField(upload_to='uploads/%Y/%m/%d')
    #test_FilePathField = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
    test_FloatField = models.FloatField(default=0.0)
    test_ImageField = models.ImageField(upload_to='uploads/%Y/%m/%d')
    test_IntegerField = models.IntegerField()
    test_GenericIPAddressField = models.GenericIPAddressField(default='192.168.1.1')
    test_NullBooleanField = models.NullBooleanField()
    test_PositiveIntegerField = models.PositiveIntegerField()
    test_PositiveSmallIntegerField = models.PositiveSmallIntegerField()
    test_SlugField = models.SlugField()
    test_SmallIntegerField = models.SmallIntegerField()
    test_TextField = models.TextField()
    test_TimeField = models.TimeField(auto_now_add=True)
    test_URLField = models.URLField()
    test_UUIDField = models.UUIDField(default=uuid.uuid4)

    # Relationship
    test_ForeignKey = models.ForeignKey(
        User,
        related_name='user_testfield_foreign_key'
    )
    test_ManyToManyField = models.ManyToManyField(
        User,
        related_name='user_testfield_many_to_many_field'
    )
    # test_OneToOneField = models.OneToOneField(
    #    User,
    #    related_name='user_testfield_one_to_one_field'
    #)
    # test_OneToManyField = models.OneToManyField(
    #    User,
    #    related_name='user_testfield_one_to_many_field'
    #)

    def __str__(self):
        return "{0} - with id {1}".format(
            self.test_CharField,
            self.pk
        )

    class Meta:
        ordering = ['-test_DateTimeField']
