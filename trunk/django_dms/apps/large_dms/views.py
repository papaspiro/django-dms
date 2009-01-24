from django_dms.views import DocumentView, DocumentAdmin
from django_dms.apps.large_dms.models import Document, DocumentInteraction
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


class DocumentEmailUploader(DocumentAdmin):
    model = Document
    email_populate = { 'email_content': 'summary', 
                       'email_subject': 'title' }
    document_view = document_view
document_email_uploader = DocumentEmailUploader(name="document_email_uploader")


# Track document interactions by registering one whenever a signal is sent
from django_dms.signals import document_interaction
document_interaction.connect(DocumentInteraction.objects.register)
