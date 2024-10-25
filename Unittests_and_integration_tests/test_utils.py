#!/usr/bin/env python3
"""  Parameterize a unit test"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test """
    """ @parameterized.expand to test the function for following inputs"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, answer):
        """ to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    """ to test that a KeyError is raised for the following inputs """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])

    def test_access_nested_map_exception(self, nested_map, path):
        """ Implement TestAccessNestedMap.test_access_nested_map_exception"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])

class TestGetJson(unittest.TestCase):
    """ test """
    """ Mock HTTP calls"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """method to test that utils.get_json returns the expected result."""
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """ Test the memoize decorator"""

    def test_memoize(self):
        """Test Memoize"""
        class TestClass:
            """ TestClass """
            def a_method(self):
                """ a method  """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()
