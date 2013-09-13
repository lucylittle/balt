# encoding: utf-8
'''
Copyright (c) 2013 Safari Books Online. All rights reserved.
'''
from django.db import models


class BaseModel(models.Model):
    '''Base class for all models'''
    created_time = models.DateTimeField('date created', auto_now_add=True)
    last_modified_time = models.DateTimeField('last-modified', auto_now=True, db_index=True)

    class Meta:
        abstract = True

class Tutorial(BaseModel):
    '''A complete Tutorial'''
    fpid = models.CharField(max_length=200, unique=True, null=True, blank=False, help_text="The FPID assigned to this Tutorial document")
    title = models.CharField(max_length=2000, help_text="The title of the Tutorial", db_index=True, null=False, blank=False)
    short_description = models.TextField(blank=True, null=True, default=None, help_text="Very short description, for list pages")
    description = models.TextField(blank=True, null=True, default=None, help_text="Front matter or introductory text")

    def __unicode__(self):
        return u"Tutorial %s" % self.title

    class Meta:
        ordering = ['title']
