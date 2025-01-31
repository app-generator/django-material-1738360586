# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    book = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Format(models.Model):

    #__Format_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Format_FIELDS__END

    class Meta:
        verbose_name        = _("Format")
        verbose_name_plural = _("Format")


class Book(models.Model):

    #__Book_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")



#__MODELS__END
