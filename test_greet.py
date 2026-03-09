import unittest
from greeter import greet

class TestGreet(unittest.TestCase):
    def test_greet_with_valid_name(self):
        self.assertEqual(greet(""), "Hello, Alice!")

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
