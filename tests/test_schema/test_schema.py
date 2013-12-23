# -*- encoding: utf-8 -*-
"""
    test.schema.schema
    ------------------

    :copyright: (c) 2013 by Morgan Delahaye-Prat.
    :license: BSD, see LICENSE for more details.
"""


from __future__ import absolute_import
from __future__ import unicode_literals

import jsonschema
from .base import SanityCheck, CheckBaseProperties, CheckCacheMechanism
from .container import CheckContainerProperties, CheckDataValidation, \
                       CheckMerging, CheckPropertyAccess

from nose.tools import assert_true, assert_equal
from flask_triangle.schema import Schema, Object


class TestSchema(SanityCheck, CheckBaseProperties, CheckCacheMechanism):
    """
    Execute all the base tests.
    """
    def setup(self):
        self.item = Schema()


class TestSchemaContainerProperties(CheckContainerProperties,
                                    CheckDataValidation,
                                    CheckPropertyAccess):
    """
    Test the common properties of the containers.
    """
    def setup(self):
        self.item = Schema()


class TestSchemaMerging(CheckMerging):
    """
    Test the common properties of the containers.
    """
    def setup(self):
        self.a = Schema()
        self.b = Schema()


class TestSchemaSpecific(object):
    """
    Test the object hierarchy of Schema / Object
    """

    def test_subclass(self):
        """
        A Schema is a specific Object
        """
        assert_true(issubclass(Schema, Object))

    def test_schema_title(self):
        """
        The schema has a specific title property.
        """
        assert_equal('ok', Schema(title='ok').schema['title'])

    def test_schema_description(self):
        """
        The schema has a specific title property.
        """
        assert_equal('ok', Schema(description='ok').schema['description'])
