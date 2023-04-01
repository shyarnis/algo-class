from brute_force_string_match import brute_force_string_match
import unittest

class TestBruteForceStringMatch(unittest.TestCase):

    def test_pattern_found(self):
        text = "Saturday is a holiday"
        pattern = "is"
        self.assertEqual(brute_force_string_match(text, pattern), 9)
    
    def test_pattern_not_found(self):
        text = "design and analysis techniques"
        pattern = "dynamic"
        self.assertEqual(brute_force_string_match(text, pattern), -1)
    
    def test_pattern_text_same(self):
        text = "sunday monday"
        pattern = "sunday monday"
        self.assertEqual(brute_force_string_match(text, pattern), 0)

if __name__ == "__main__":
    unittest.main()