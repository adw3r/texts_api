import unittest

from text import get_texts_json, Text, get_referals_json, get_referals_response


class TestText(unittest.TestCase):

    def test_text_init(self):
        link = 'google.com'
        text = Text('ru', link, 'SuperCat')

        get_text = text.get_text()
        print(get_text)
        self.assertTrue(link in get_text)

    def test_get_referals_response(self):
        response = get_referals_response()
        print(response.json()['SuperCat'])

    def test_get_texts_json(self):
        texts_json = get_texts_json()
        self.assertTrue(isinstance(texts_json, dict))

    def test_get_referals_json(self):
        values = get_referals_json()
        print(values.get('SuperCat').get('spins'))
        self.assertTrue(isinstance(values, dict))
