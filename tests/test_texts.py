import unittest

from texts_module.module.text import get_texts, Text


class TestText(unittest.TestCase):

    def test_get_texts(self):
        texts_json = get_texts()
        self.assertTrue(isinstance(texts_json, dict))

    def test_text_init(self):
        link = 'google.com'
        text = Text('ru', link, 'allright')

        get_text = text.get_text()
        self.assertTrue(link in get_text)
