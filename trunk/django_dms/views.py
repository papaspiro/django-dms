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

