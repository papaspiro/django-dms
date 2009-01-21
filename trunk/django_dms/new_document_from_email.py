#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: 
    Project: 
     Author: Will Hardy
       Date:  2008
      Usage: 
  $Revision$

Description: Accepts an email from standard input or the given filename and adds it or prepares the document to be added.

     Design:

            * Allow developer to specify model and staging model (if any)
            * Email reply with a link (uuid encoded) to edit the document

"""
import os.path
from StringIO import StringIO
from email import message_from_file
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def receive_document(data, site=None):
    if site:
        mod_name, obj_name = get_mod_obj(site)
        if obj_name != '':
            site = getattr(__import__(mod_name, {}, {}, ['']), obj_name)

    # Get the target model (usually the supplied staging model)
    if getattr(settings, 'DJANGO_DMS_STAGING', True):
        from django_dms.models import DocumentStaging as model
    else:
        model = site.model

    # Extract data from the email
    email = message_from_file(data)
    # Save the files to the system
    documents = get_documents(email, model)

    from django.contrib.sites.models import Site
    host = 'http://%s' % Site.objects.get_current().domain
    message = EmailMessage()
    message.to = email.get('Reply-To', email['From'])
    message.subject = "Attachments received" # TODO allow customisation of this 
    message.body = render_to_string('django_dms/staged_document.txt', {'host': host,'dms_site': site, 'email': email, 'documents': documents})
    #message.send()

    print message.body


def get_subject_content(email):
    """ Extraact the subject and plain text body of an email. """
    # TODO: HTML emails!

    email_subject = email.get('Subject', "Untitled")
    email_content = ""
    for part in email.get_payload():
        # TODO: Is there a better way to do this test?
        if not part.get_filename() and part.get_content_type() == 'text/plain':
            email_content = part.get_payload(decode=True)
            break
    return (email_subject, email_content)

def get_documents(email, model):
    """ Add documents to system and return a list of instances. """
    email_subject, email_content = get_subject_content(email)

    documents = []
    for part in email.get_payload():
        if part.get_filename():
            documents.append(model.objects.add_staging_document(part.get_payload(decode=True), 
                                part.get_filename(), part.get_content_type(), email_subject, email_content))
    return documents

def get_mod_obj(path):
    try:
        dot = path.rindex('.')
    except ValueError:
        return path, ''
    return path[:dot], path[dot+1:]


if __name__ == '__main__':
    email = open('/Users/will/Desktop/test.eml', 'r')
    receive_document(email, site='documents.views.legal_essay_admin')


