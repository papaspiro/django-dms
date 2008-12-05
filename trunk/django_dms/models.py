#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: DMS framework models
    Project: django_dms
     Author: Will Hardy
       Date: November 2008
  $Revision$
"""

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.encoding import force_unicode, smart_unicode

from documents.utils import ChoicesBank, UUIDField, HashField, get_hash

class DocumentBase(models.Model):
    """ Minimum fields for a document entry.
        Inherit this model to customise document metadata, see BasicDocument for an example.
    """
    uuid         = models.CharField(max_length=36, default=lambda:unicode(uuid.uuid4()), blank=True, editable=False, primary_key=True)
    file         = models.FileField(upload_to=lambda i,f: 'documents/%s' % i.uuid)
    mimetype     = models.CharField(max_length=80, default="", blank=True)

    date_added   = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save_file(self, contents, save=False):
        " Save a file, creating a new document_version if necessary. "
        self.file.save(contents.name, contents, save=save)

    def __unicode__(self):
        return self.uuid


class BasicDocumentBase(DocumentBase):
    """ Basic document entry, with a selected metadata.
    """
    title        = models.CharField(max_length=150, default="", blank=True)
    summary      = models.TextField(default="", blank=True)
    author       = models.CharField(max_length=150, default="", blank=True)
    date_created = models.DateTimeField(null=True, blank=True)

    # NB: Automate this in the form
    uploaded_by  = models.ForeignKey(User, null=True, blank=True, editable=False)

    # Extract plaintext from document and store in database to allow full-text searching
    plaintext    = models.TextField(default="", blank=True, editable=False)

    def __unicode__(self):
        return self.title or 'untitled (%s...%s)' % (self.uuid[:3], self.uuid[-3:])

    class Meta:
        abstract = True


    # METADATA handling fields

    AUTO_METADATA = dict(title='title', mimetype='mimetype', author='creator', date_created='creation date')
    def process_metadata_title(self, value):
        return value.isupper() and value.title() or value
    def process_metadata_date_created(self, value):
        for pattern in ('%Y-%m-%dT%H:%M:%SZ', '%Y%m%d%H%M%S'):
            try:
                # String is trimmed to the size of pattern, assuming that
                # it is the same length as the string it is matching (coincidently, it often is!).
                return datetime.strptime(value[:len(pattern)], pattern)
            except ValueError:
                continue
        return value
