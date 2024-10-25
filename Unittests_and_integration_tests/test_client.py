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

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_json, moc_test):
        """TestGithubOrgClient.test_public_repos"""
        test = {'name': 'hello'}
        mock_json.return_value = test
        client = GithubOrgClient('hello')
        result = client._public_repos_url()
        self.assertEqual(test, result)
        
    @parameterized.expand([({"license": {"key": "my_license"}}, "my_license",True),
                            ({"license": {"key": "other_license"}},"my_license",False),])
    @patch('client.GithubOrgClient.has_license')
    def test_has_license(self, license, license_key, bool, mock_has):
        """7. Parameterize"""
        client = GithubOrgClient('test')
        result = client.has_license(license, license_key)
        self.assertEqual(result, result)
