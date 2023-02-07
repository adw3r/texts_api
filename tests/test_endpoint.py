import unittest

import requests

from config import PORT


class TestEndpoint(unittest.TestCase):

    def test_get_text(self):
        link = 'google.com'
        params = {
            'lang': 'ru',
            'link': link,
            'refname': 'AllRight'
        }
        url = f'http://localhost:{PORT}/text'

        resp = requests.get(url, params=params)
        self.assertTrue(link in resp.text)

    def test_get_test_text(self):
        link = 'google.com'
        params = {
            'lang': 'ru',
            'link': link,
            'refname': 'AllRight'
        }
        url = f'http://localhost:{PORT}/text'

        resp = requests.get(url, params=params)
        text = resp.text
        self.assertTrue(link in text)
        self.assertTrue(text in text)
