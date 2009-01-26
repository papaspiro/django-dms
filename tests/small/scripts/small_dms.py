#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# ./manage.py dumpscript small_dms

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():

    from django_dms.apps.small_dms.models import Document
    from django.core.files.base import ContentFile, File

    small_dms_document_1 = Document()
    small_dms_document_1.file.save('a.pdf', ContentFile(open(u'../large/media/documents/30e114f9-6819-4712-9eb8-2a20ce796ddb.pdf').read()), save=False)
    small_dms_document_1.file_mimetype = u'application/pdf'
    small_dms_document_1.file_extension = u'.pdf'
    small_dms_document_1.date_added = datetime.datetime(2009, 1, 26, 1, 39, 9, 882697)
    small_dms_document_1.date_updated = datetime.datetime(2009, 1, 26, 1, 48, 9, 594448)
    small_dms_document_1.title = u'Aliquam erat volutpat'
    small_dms_document_1.slug = u'aliquam-erat-volutpat'
    small_dms_document_1.summary = u'Sed accumsan. Curabitur interdum. Sed pulvinar, nisl eget lacinia congue, risus nibh elementum nibh, vitae congue arcu mauris ut neque. Praesent ut ante at est egestas luctus. Etiam blandit auctor lacus. Cras vulputate laoreet lectus. Suspendisse potenti. Mauris vitae ante sit amet tortor condimentum lobortis. Nunc eu velit ac nibh aliquet semper. Nullam commodo dignissim ligula. Maecenas aliquam facilisis turpis. Suspendisse ante. Praesent ornare. Fusce est lorem, ornare euismod, ultrices vitae, molestie non, risus. Maecenas diam. Integer tincidunt nisi a nulla. Proin commodo velit quis urna. Curabitur et tortor. Nunc sodales lacinia tellus.'
    small_dms_document_1.plaintext = u''
    small_dms_document_1.save()

    small_dms_document_2 = Document()
    small_dms_document_2.file.save('a.pdf', ContentFile(open(u'../large/media/documents/a72ddf11-fcb3-41b7-ae2f-3716328755f1.pdf').read()), save=False)
    small_dms_document_2.file_mimetype = u'application/pdf'
    small_dms_document_2.file_extension = u'.pdf'
    small_dms_document_2.date_added = datetime.datetime(2009, 1, 26, 1, 40, 10, 777492)
    small_dms_document_2.date_updated = datetime.datetime(2009, 1, 26, 1, 48, 5, 106479)
    small_dms_document_2.title = u'Aenean diam erat'
    small_dms_document_2.slug = u'aenean-diam-erat'
    small_dms_document_2.summary = u'Mattis eu, consectetur ac, faucibus a, elit. Phasellus viverra arcu facilisis sem. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque cursus porta erat. Aenean sem. Proin interdum odio et sem. Etiam vitae velit. Praesent ante leo, gravida vitae, tincidunt ac, eleifend bibendum, velit. Pellentesque vestibulum ligula sit amet elit. Suspendisse lorem ipsum, pharetra sit amet, lobortis vitae, iaculis eget, mauris. Cras viverra. Sed aliquet. Nulla facilisi. Phasellus nibh justo, hendrerit tincidunt, rhoncus ac, viverra eget, sapien.'
    small_dms_document_2.plaintext = u''
    small_dms_document_2.save()

    small_dms_document_3 = Document()
    small_dms_document_3.file.save('a.pdf', ContentFile(open(u'../large/media/documents/0be0d87a-589e-4679-ad27-6d693642e31d.pdf').read()), save=False)
    small_dms_document_3.file_mimetype = u'application/pdf'
    small_dms_document_3.file_extension = u'.pdf'
    small_dms_document_3.date_added = datetime.datetime(2009, 1, 26, 1, 41, 2, 5902)
    small_dms_document_3.date_updated = datetime.datetime(2009, 1, 26, 1, 48, 0, 909089)
    small_dms_document_3.title = u'Phasellus semper porta ligula'
    small_dms_document_3.slug = u'phasellus-semper-porta-ligula'
    small_dms_document_3.summary = u'Duis nisi. Ut sed ante vel felis tempor elementum. Quisque ultrices porttitor ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Maecenas feugiat eleifend tortor. Praesent orci ligula, mattis quis, ultrices id, placerat non, mi. Nam id mauris. Vivamus porttitor. Vestibulum quis ligula.'
    small_dms_document_3.plaintext = u''
    small_dms_document_3.save()

    small_dms_document_4 = Document()
    small_dms_document_4.file.save('a.pdf', ContentFile(open(u'../large/media/documents/e881e0c0-0982-4194-8a61-2cd5c3b05a95.pdf').read()), save=False)
    small_dms_document_4.file_mimetype = u'application/pdf'
    small_dms_document_4.file_extension = u'.pdf'
    small_dms_document_4.date_added = datetime.datetime(2009, 1, 26, 1, 45, 28, 788381)
    small_dms_document_4.date_updated = datetime.datetime(2009, 1, 26, 1, 47, 54, 900525)
    small_dms_document_4.title = u'Cras eros ipsum, auctor quis, ullamcorper ut'
    small_dms_document_4.slug = u'cras-eros-ipsum'
    small_dms_document_4.summary = u'Vestibulum cursus. Sed nec lorem. Maecenas elementum, metus in scelerisque cursus, est diam lobortis nisi, nec facilisis justo enim vitae mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam erat volutpat. Donec molestie, sem malesuada faucibus bibendum, turpis neque sodales velit, sit amet pharetra dui mi eget lectus.'
    small_dms_document_4.plaintext = u''
    small_dms_document_4.save()

    small_dms_document_5 = Document()
    small_dms_document_5.file.save('a.pdf', ContentFile(open(u'../large/media/documents/95d12669-e6c8-459b-b4d8-437b2e36a027.pdf').read()), save=False)
    small_dms_document_5.file_mimetype = u'application/pdf'
    small_dms_document_5.file_extension = u'.pdf'
    small_dms_document_5.date_added = datetime.datetime(2009, 1, 26, 1, 46, 31, 869004)
    small_dms_document_5.date_updated = datetime.datetime(2009, 1, 26, 1, 47, 48, 839881)
    small_dms_document_5.title = u'Proin quis mi'
    small_dms_document_5.slug = u'proin-quis-mi'
    small_dms_document_5.summary = u'Mauris et urna id elit rhoncus feugiat. Cras quis mauris in orci mattis volutpat. Integer nisl pede, tristique in, dictum vel, consectetur volutpat, velit. Donec congue, pede quis vehicula posuere, elit eros venenatis urna, sit amet pharetra nisi lorem et ligula. Donec a mauris ac magna vulputate blandit. Curabitur eu quam. Pellentesque vehicula laoreet diam.'
    small_dms_document_5.plaintext = u''
    small_dms_document_5.save()

    small_dms_document_6 = Document()
    small_dms_document_6.file.save('a.pdf', ContentFile(open(u'../large/media/documents/44134c09-53dc-4ce8-aa74-cc193b209c7c.pdf').read()), save=False)
    small_dms_document_6.file_mimetype = u'application/pdf'
    small_dms_document_6.file_extension = u'.pdf'
    small_dms_document_6.date_added = datetime.datetime(2009, 1, 26, 1, 47, 42, 403985)
    small_dms_document_6.date_updated = datetime.datetime(2009, 1, 26, 1, 47, 42, 406140)
    small_dms_document_6.title = u'Quisque ullamcorper tincidunt eros'
    small_dms_document_6.slug = u'quisque-ullamcorper-tincidunt-eros'
    small_dms_document_6.summary = u'Morbi leo. Aenean nisl ante, tristique nec, lobortis eu, tincidunt id, magna. Mauris accumsan ligula sit amet felis. Nulla ornare, augue sed egestas aliquet, nunc ligula dapibus augue, eget tempus ipsum est quis mauris. In elit magna, porta nec, tincidunt in, rutrum nec, libero. Nulla facilisi. Mauris faucibus cursus tellus. Donec adipiscing dui sit amet tellus. Nunc nibh sem, porta vitae, sodales eu, blandit fermentum, velit.'
    small_dms_document_6.plaintext = u''
    small_dms_document_6.save()


