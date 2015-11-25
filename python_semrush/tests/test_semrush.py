# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os
from unittest import TestCase
from python_semrush.semrush import SemrushClient


class SemrushTestCase(TestCase):

    def test_parse_response(self):
        with open(os.path.join(os.path.dirname(__file__), 'response.txt'), 'rb') as f:
            response = SemrushClient.parse_response(f.read())
            print(response)
        self.fail()
