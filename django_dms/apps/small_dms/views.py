from django_dms.views import DocumentView, DocumentAdmin
from django_dms.apps.small_dms.models import Document
from django.db import models
from django.contrib.humanize.templatetags.humanize import naturalday

class DocumentView(DocumentView):
    list_display = ['author', 'summary']
    list_thumbnail = False
    thumbnail = True
    queryset = Document.objects.all()
    fields = ['author', 'summary', 'date_created', 'uploaded_by']
    ordering = ['title']
    url_identifier_field = 'slug'
    field_class_filters = { models.DateTimeField: lambda v: naturalday(v, 'F Y').title() }

document_view = DocumentView(name="document_view")
