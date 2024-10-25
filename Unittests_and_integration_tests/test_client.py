#!/usr/bin/env python3
"""
In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase)
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ test """
    @parameterized.expand([("google"),("abc"),])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, expected_response,mock_get_json):
        """ test that GithubOrgClient.org returns the correct value """
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
