#!/usr/bin/env python
# encoding: utf-8
"""
Created by Andrew Brookins on Sep 03 11:50 AM 2013
Copyright (c) 2013 Safari Books Online. All rights reserved.
"""

from django.conf.urls import patterns, url


urlpatterns = patterns('tutorials.views',
                       url(r'^$', 'tutorial_list', name='index'),
)

