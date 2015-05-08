#!/usr/bin/env python

from __future__ import print_function

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
except ImportError as e:
    import unittest2 as unittest
    import mock
    from mock import patch

from clorg.main import main

class TestMain(unittest.TestCase):
    def test_true_is_true(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
