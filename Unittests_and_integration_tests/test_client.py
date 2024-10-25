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
    @parameterized.expand([("google"), ("abc"),])
    @patch("client.get_json", value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """ test that GithubOrgClient.org returns the correct value """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get_json.value)
        mock_get_json.assert_called_once

    def test_public_repos_url(self, mock_org):
        """test_public_repos_url method"""

        test_url = f'https://api.github.com/orgs/test/repo'

        mock_org.return_value = {'repos_url': test_url}

        client = GithubOrgClient('test')
        result = client._public_repos_url()

        self.assertEqual('https://api.github.com/orgs/test/repo', test_url)
