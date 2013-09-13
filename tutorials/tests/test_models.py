# encoding: utf-8
'''
Copyright (c) 2013 Safari Books Online. All rights reserved.
'''

from django.test import TestCase


from tutorials import models


class TestTutorials(TestCase):
    def setUp(self):
        self.tutorial = models.Tutorial.objects.create(title="The Title", fpid="The FPID")
        self.tutorial2 = models.Tutorial.objects.create(title="The Title 2", fpid="The other FPID")

    def test_tutorials_have_unicode_method(self):
        '''The Tutorial should have a __unicode__ method.'''
        expected = 'Tutorial {}'.format(self.tutorial.title)
        self.assertEquals(expected, unicode(self.tutorial))
