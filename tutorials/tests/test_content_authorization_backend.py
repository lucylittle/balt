#!/usr/bin/env python
# encoding: utf-8
"""
Created by Andrew Brookins on Sep 04 10:54 AM 2013
Copyright (c) 2013 Safari Books Online. All rights reserved.
"""
import uuid


from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase


import nest.models


from tutorials import models, content_authorization


class TestContentAuthorizationBackend(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", email="user@example.com",
                                             password="password")
        self.group = models.Group.objects.create(title="The Group")
        tutorial = models.Tutorial.objects.create(title="The Title", group=self.group)
        topic = models.Topic.objects.create(tutorial=tutorial, order=0)
        self.document = nest.models.EpubArchive.objects.create(
            title='Title', identifier='identifier{}'.format(uuid.uuid4()))
        self.hf = nest.models.HTMLFile.objects.create(archive=self.document, filename="1")
        lesson = models.Lesson.objects.create(topic=topic, tutorial=tutorial, htmlfile=self.hf,
                                              order=1)
        self.account = models.Account.objects.create(name=str(uuid.uuid4()), subdomain='here')

    def test_allowed_if_account_can_access(self):
        '''The content authorization backend should allow a user to access an EpubArchive if the user's Account has access to the archive.'''
        self.account.users.add(self.user)
        self.account.groups.add(self.group)
        expected = True
        allowed = content_authorization.check_full_authorization(self.user, self.document)
        self.assertEqual(expected, allowed)

    def test_not_allowed_if_account_cannot_access(self):
        '''The content authorization backend should not allow a user to view an EpubArchive if the user's Account does not have access to the archive.'''
        self.account.users.add(self.user)
        self.account.groups.remove(self.group)
        expected = False
        allowed = content_authorization.check_full_authorization(self.user, self.document)
        self.assertEqual(expected, allowed)

    def test_not_allowed_if_no_groups(self):
        '''The content authorization backend should not allow a user to view an EpubArchive if the user's account has no Groups.'''
        self.account.users.remove(self.user)
        expected = False
        allowed = content_authorization.check_full_authorization(self.user, self.document)
        self.assertEqual(expected, allowed)

    def test_not_allowed_if_not_authenticated(self):
        '''The content authorization backend should not allow an anonymous user to view an EpubArchive.'''
        expected = False
        allowed = content_authorization.check_full_authorization(AnonymousUser(), self.document)
        self.assertEqual(expected, allowed)
