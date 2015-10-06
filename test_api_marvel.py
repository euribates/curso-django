#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import unittest
import api_marvel

class Uso(unittest.TestCase):

    def test_calc_hash(self):
        self.assertEqual(
            api_marvel.calc_hash(1), 
            '76f9dbf34ff5941d4bbca23a759e8613',
            )

    def test_find_character(self):
        r = api_marvel.find_character('falcon')
        for c in r['data']['results']:
            print(c['name'], c['description'])
            print(c.keys())

if __name__ == '__main__':
    unittest.main()
