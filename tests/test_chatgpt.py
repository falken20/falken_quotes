import unittest

from falken_quotes import chatgpt


class TestChatGPT(unittest.TestCase):

    def test_translate(self):
        text_to_translate = "Hello"
        response = chatgpt.translate(text_to_translate=text_to_translate)

        print(response)
        self.assertTrue(False)