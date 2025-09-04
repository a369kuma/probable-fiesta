import unittest
from gpt3 import Code

class TestCode(unittest.TestCase):
    def setUp(self):
        self.code = Code({}, {}, "http://tinyurl.com/")

    def test_encode_unique_urls(self):
        url1 = "https://example.com"
        url2 = "https://another.com"
        short1 = self.code.encode(url1)
        short2 = self.code.encode(url2)
        self.assertNotEqual(short1, short2)
        self.assertEqual(self.code.decode(short1), url1)
        self.assertEqual(self.code.decode(short2), url2)

    def test_encode_duplicate_url(self):
        url = "https://example.com"
        short1 = self.code.encode(url)
        short2 = self.code.encode(url)
        self.assertEqual(short1, short2)

    def test_decode_invalid_url(self):
        with self.assertRaises(ValueError):
            self.code.decode("http://tinyurl.com/invalid")

    def test_empty_url(self):
        with self.assertRaises(ValueError):
            self.code.encode("")

if __name__ == "__main__":
    unittest.main()
