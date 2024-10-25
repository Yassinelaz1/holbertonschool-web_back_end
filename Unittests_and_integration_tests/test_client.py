#!/usr/bin/env python3
"""
5. Mocking a property
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    """ test """
    @parameterized.expand([("google"),("abc"),])
    @patch("client.get_json", return_value={"payload": True})
    def test_access_nested_map_exception(self, nested_map, path):
        """ 5. Mocking a property"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])
