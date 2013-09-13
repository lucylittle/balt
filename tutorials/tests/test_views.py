#!/usr/bin/env python
# encoding: utf-8
"""
Created by Andrew Brookins on Sep 03 2:15 PM 2013
Copyright (c) 2013 Safari Books Online. All rights reserved.
"""
import uuid

from lxml import etree
from lxml.html import document_fromstring, html5parser

from django.core.urlresolvers import reverse
from django.test import TestCase


from tutorials import models


class TestIndexView(TestCase):

    def test_index_shows_all_tutorials(self):
        '''The Tutorial index should show all tutorial groups when not on a subdomain that matches an Account.'''

        expected = [str(uuid.uuid4()),
                    str(uuid.uuid4()),
                   ]
        for e in expected:
            models.Tutorial.objects.create(title=e, fpid=e)

        resp = self.client.get(reverse('index'))
        html5 = html5parser.document_fromstring(resp.content)
        nodes = document_fromstring(etree.tostring(html5))
        expected = models.Group.objects.count()

        num_titles = len(nodes.cssselect('.t-tutorial-title'))
        self.assertEqual(expected, num_titles)
