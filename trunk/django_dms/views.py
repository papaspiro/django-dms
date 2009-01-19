#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: 
    Project: 
     Author: Will Hardy
       Date:  2008
      Usage: 
  $Revision$

Description: 

"""
import threading
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class DocumentResponse(HttpResponse):
    def __init__(self, document):
        super(DocumentResponse, self).__init__(content=document.file, mimetype=document.file_mimetype or 'text/plain')
        self['Content-Disposition'] = 'attachment; filename=%s' % document.friendly_filename

class DocumentViewResponse(HttpResponse):
    """ If we can show a thumbnail (eg the first page of a PDF), do that, otherwise download the document in-browser. """
    def __init__(self, document):
        super(DocumentViewResponse, self).__init__(content=document.file, mimetype=document.file_mimetype or 'text/plain')

def email_document(document, to, template='django_dms/email.txt', subject=''):
    """ Email the given document to the given email address.
    """
    # Start a new thread to email the document
    # This avoids a frozen screen while the email is being sent (particularly if the document is big).
    t = threading.Thread(target=_email_document, args=[document, to, template, subject])
    t.setDaemon(True)
    t.start()

def _email_document(document, to, template='django_dms/email.txt', subject=''):
    """ Helper function to email document in another thread.
    """ 
    # TODO: A really cool system would delay sending the email for 10 seconds or so, 
    # to allow the user to quickly undo :-) This could probably also be done client-side (ie JS)
    # Create the message
    message = EmailMessage(to=to, subject=subject)
    message.to = to
    message.subject = subject
    message.body = render_to_string(template, {'document': document})
    message.attach(document.friendly_filename, document.file.read(), document.file_mimetype)

    # Send the message
    message.send()
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from django.db.models import Count


class Item():
    pass

class DocumentView(HttpResponse):
    queryset = None
    list_template = 'django_dms/list.html'
    list_thumbnail = True
    list_display = ['summary']
    list_links = ['preview', 'view', 'download', 'email']
    list_per_page = 10
    ordering = None # TODO
    search_fields = None # TODO
    fields = None # TODO
    exclude = None # TODO

    def __init__(self, name=None):
        " Object instanciation can emulate a view, by passing a request object. "

        super(DocumentView, self).__init__()
        self.name = name
        self._is_string = True

    def list_view(self, request):
        self.request = request
        self.page_number = request.GET.get('page', 1)
        # Clear the queryset cache to force a new query each time
        # NB this is an internal attribute, but clearing the cache is necessary
        self.queryset._result_cache = None

        return HttpResponse(self.content)

    @property
    def content(self):
        return loader.render_to_string(self.list_template, self.context)

    def get_list_item(self, document):
        """ Get an item for the template, containing the document. """
        list_item = Item()
        list_item.document = document
        # TODO: call callables?
        list_item.display_fields = [(document._meta.get_field(field).verbose_name, getattr(document, field)) for field in self.list_display ]
        return list_item

    @property
    def context(self):
        #documents = self.queryset.values_list(*self.list_display)
        pages = Paginator(self.queryset, self.list_per_page)
        page = pages.page(self.page_number)
        object_list = [ self.get_list_item(i) for i in page.object_list ]
        context = { 'request': self.request, 'object_list': object_list, #TODO: use pages properly
                    'list_display': dict([(a, True) for a in self.list_display]),
                    'list_thumbnail': self.list_thumbnail,
                    'list_links': dict([(a, True) for a in self.list_links]),
                    'page': page,
                    'dms_site': self.name,
                    }
        return context

    # Process documents before use
    def _set_documents(self, documents):
        # Add annotations
        self._documents = documents.annotate(already_sent=Count('interactions'))
    documents = property(lambda s:s._documents, _set_documents)


    def get_urls(self):
        from django.conf.urls.defaults import patterns, url, include
        print self.name

        return patterns('',
            url(r'^$',                      self.list_view, name="%s_index" % self.name),
            url(r'^download/([\w\d-]+)/$',  self.download, name="%s_document_download" % self.name),
            url(r'^send/([\w\d-]+)/$',      self.send, name="%s_document_send" % self.name),
            url(r'^send/([\w\d-]+)/ajax/$', self.send_ajax, name="%s_document_send_ajax" % self.name),
            url(r'^detail/([\w\d-]+)/$',    self.detail, name="%s_document_detail" % self.name),
            url(r'^view/([\w\d-]+)/$',      self.view, name="%s_document_view" % self.name),
            )
    urls = property(lambda s: s.get_urls())

    def download(self, request):
        pass
    def send(self, request):
        pass
    def send_ajax(self, request):
        pass
    def detail(self, request):
        pass
    def view(self, request):
        pass
