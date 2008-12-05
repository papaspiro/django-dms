#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: DMS framework utilities
    Project: django_dms
     Author: Will Hardy
       Date: November 2008
  $Revision$

"""
import uuid
import hashlib
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode, smart_unicode

class ChoicesBank(object):
    """ Allows individual objects to be chosen from choices, without needing the entire queryset.
        This lets the Widget decide which values will be used.
    """
    def __init__(self, queryset):
        self.queryset = queryset

    def only(self, keys):
        return ((key, smart_unicode(val)) for key, val in self.queryset.in_bulk(keys).iteritems())

    def __iter__(self):
        """ Emulate standard choices object. """
        return ((x._get_pk_val(), smart_unicode(x)) for x in self.queryset)

    def __len__(self):
        return len(self.queryset)

def get_hash(content):
    return hashlib.sha224(content.read()).hexdigest()

class HashField(models.CharField):
    """ Store a hash of the given field.
    """
    def __init__(self, from_field, *args, **kwargs):
        kwargs.setdefault('max_length', 56)
        super(HashField, self).__init__(*args, **kwargs)
        self.from_field = from_field

    def pre_save(self, model_instance, add):
        """ Generate the hash on save. 
        """
        # TODO: When/how often should the hash be generated? every save?
        return get_hash(getattr(model_instance, self.from_field))

    def get_internal_type(self):
        return models.CharField.__name__



# The following field isn't necessary, but is useful for those who just want a UUID field

class UUIDField(models.CharField):
    """ UUIDField
    For convenience and reuse, this is equivalent to:
        models.CharField(max_length=36, default=lambda:unicode(uuid.uuid4()), blank=True, editable=False)

    By using "default", the value is there from the beginning, before the model is saved.
    A better implementation might store the value as an 128 bit integer in the database.
    For more information see: http://docs.python.org/lib/module-uuid.html
    """

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36
        kwargs.setdefault('default', lambda: unicode(uuid.uuid4()))
        kwargs.setdefault('blank', True)
        kwargs.setdefault('editable', False)
        super(UUIDField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return models.CharField.__name__
