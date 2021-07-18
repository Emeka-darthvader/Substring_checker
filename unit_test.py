import unittest
from substring_checker import SubstringChecker

class TestSubstringChecker(unittest.TestCase):
    def test_longest_substring(self):
        substring_checker = SubstringChecker("abcabcdc") ## Ensuring palindrome works
        another_substring_checker = SubstringChecker("bbbbb") ##testing for case sensitivity too
        assert substring_checker.get_length_longest_substring() == 'abcd',"Should be false as Emeka is not a palindrome"
        assert another_substring_checker.get_length_longest_substring() == 'b',"Should be True as Ada is a palindrome"


if __name__ == "__main__":
    unittest.main()