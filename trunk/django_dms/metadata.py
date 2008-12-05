#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: Metadata extractor
    Project: django_dms
     Author: Will Hardy
       Date: November 2008
  $Revision$

"""

import extractor as libextractor
extractor = libextractor.Extractor(lang="en")

def extract_metadata(sender, instance, force=False):
    """ Extract and populate metadata from the file itself.
        @force: Overwrite existing metadata
    """
    if not extractor:
        return

    all_keywords = extractor.extract(data=instance.file.read(), size=instance.file.size)
    keywords = dict(all_keywords)

    try:
        for attr, field in instance.AUTO_METADATA.items():
            if field in keywords and (force or not hasattr(instance, attr)):
                # 1. Extract data
                value = keywords[field].encode('iso-8859-1')

                # 2. Post-extraction processing
                try:
                    value = getattr(instance, 'process_metadata_%s' % attr)(value)
                except AttributeError:
                    # No value processing defined
                    pass

                # 3. Set the discovered value
                if value:
                    setattr(instance, attr, value)

    except AttributeError:
        # TODO: Maybe we should raise this exception
        # It can only mean a coding mistake 
        # (that is, connecting the signal without defining AUTO_METADATA)
        pass


    # TODO: Other keywords might have multiple values, it would be better to handle that properly
    if hasattr(instance, 'plaintext'):
        for key, value in all_keywords:
            if key == 'unknown':
                instance.plaintext += ' ' + value
