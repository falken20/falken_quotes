import unittest

from falken_quotes import quotes


class TestQuotes(unittest.TestCase):

    def test_get_api_quote(self):
        response = quotes.get_api_quote("falsa_url")
        self.assertEqual({}, response)
