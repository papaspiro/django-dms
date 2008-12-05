#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: Basic admin for and out-of-the-box DMS
    Project: django_dms
     Author: Will Hardy
       Date: November 2008
  $Revision$
"""

from django.contrib import admin
from documents.basicdocuments.models import BasicDocument, TestDocumentModel

class BasicDocumentAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'author', 'mimetype', 'uploaded_by', 'date_added', 'date_created')

class TestDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'document', 'uuid',)

admin.site.register(BasicDocument, BasicDocumentAdmin)
admin.site.register(TestDocumentModel, TestDocumentAdmin)
