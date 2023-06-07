import unittest

from falken_quotes import api_translate


class TestAPITranslate(unittest.TestCase):

    def test_translate(self):
        text_to_translate = "Hello"
        response = api_translate.translate(
            source="en",
            to="es", 
            text_to_translate=text_to_translate
        )
        self.assertIn("Hola", response)
