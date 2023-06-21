import unittest
from machinetranslation import translator

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hi"), "Bonjour")
        self.assertNotEqual(english_to_french("No"), "Bonjour")
        self.assertEqual(english_to_french("Yes"), "Oui")

class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()