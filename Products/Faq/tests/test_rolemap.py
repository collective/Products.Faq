# -*- coding: utf-8 -*-

from Products.Faq.testing import PLONE_FAQ_INTEGRATION_TESTING

import pkg_resources
import unittest2 as unittest

PLONE_VERSION = pkg_resources.require("Plone")[0].version
FOLDER_ROLES = ['Contributor', 'Manager', 'Site Administrator']
FAQ_ROLES = ['Contributor', 'Manager', 'Site Administrator']

if PLONE_VERSION < '4.1':  # no 'Site Administrator' role
    FOLDER_ROLES.remove('Site Administrator')
    FAQ_ROLES.remove('Site Administrator')


class RolemapTestCase(unittest.TestCase):

    layer = PLONE_FAQ_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_faq_roles(self):
        folder_roles = [r['name'] for r in self.portal.rolesOfPermission('Products.Faq: Add FaqFolder') if r['selected']]
        self.assertEqual(folder_roles, FOLDER_ROLES)
        faq_roles = [r['name'] for r in self.portal.rolesOfPermission('Products.Faq: Add FaqEntry') if r['selected']]
        self.assertEqual(faq_roles, FAQ_ROLES)
