#!/usr/bin/env python
# encoding: utf-8
"""
Created by Andrew Brookins on Sep 03 11:27 AM 2013
Copyright (c) 2013 Safari Books Online. All rights reserved.
"""

import logging


from django.shortcuts import render
from django.views.decorators.cache import never_cache


import tutorials.models


log = logging.getLogger(__name__)


@never_cache
def tutorial_list(request):
    '''
    Show a list of Tutorials 
    '''
    toots = tutorials.models.Tutorial.objects.all()
    return render(request, 'tutorials.html', {
        'tutorials': toots,
    })
