# -*- coding: utf-8 -*-
import unittest


from string_problems import reverse_words
from string_problems import group_anagrams
from string_problems import longest_substring
from string_problems import compare_version_numbers
from string_problems import find_permuted_substring


class ReverseWordsTest(unittest.TestCase):

    def test_reverse_sentence(self):
        assert reverse_words('it\'s not a tumor') == 'tumor a not it\'s'

    def test_reverse_word(self):
        assert reverse_words('bottle') == 'bottle'

    def test_reverse_empty(self):
        assert reverse_words('') == ''

    def test_reverse_whitespace(self):
        assert reverse_words(' alex chao ') == 'chao alex'


class GroupAnagramsTest(unittest.TestCase):

    def test_group_anagrams(self):
        words = ['het', 'costar', 'the', 'bottle', 'eht', 'actors']
        groups = group_anagrams(words)
        assert len(groups) == 3
        assert set(['the', 'het', 'eht']) in groups
        assert set(['actors', 'costar']) in groups
        assert set(['bottle']) in groups


class LongestSubstringTest(unittest.TestCase):

    def test_empty(self):
        assert longest_substring('abcabcbb') == 3 # 'abc'

    def test_no_repeats(self):
        assert longest_substring('abcdefgh') == 8 # 'abcdefgh'

    def test_repeated_character(self):
        assert longest_substring('bbbbb') == 1 # 'b'

    def test_continuation_of_repeated_character(self):
        assert longest_substring('pwwkew') == 3 # 'wke'

    def test_empty(self):
        assert longest_substring('') == 0 # ''

    def test_continguous(self):
        assert longest_substring('abcdaxyzb') == 7 # 'bcdaxyz'

    def test_palindrome(self):
        assert longest_substring('abba') == 2 # 'ab'


class CompareVersionNumbersTest(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(compare_version_numbers('0.1', '13.37'), -1)
        self.assertEqual(compare_version_numbers('13.37', '0.1'), 1)

    def test_no_dot_releases(self):
        self.assertEqual(compare_version_numbers('432', '432'), 0)
        self.assertEqual(compare_version_numbers('3', '29'), -1)
        self.assertEqual(compare_version_numbers('29', '3'), 1)

    def test_main_version_number(self):
        self.assertEqual(compare_version_numbers('5.123', '6.123'), -1)
        self.assertEqual(compare_version_numbers('6.123', '5.123'), 1)

    def test_same_version(self):
        self.assertEqual(compare_version_numbers('1.02', '1.02'), 0)
        self.assertEqual(compare_version_numbers('1.2', '1.2'), 0)
        self.assertEqual(compare_version_numbers('1.2', '1.20'), 0)
        self.assertEqual(compare_version_numbers('1.2', '1.2.0'), 0)
        self.assertEqual(compare_version_numbers('1.2', '1.2.0.0'), 0)
        self.assertEqual(compare_version_numbers('1.2', '1.2.00'), 0)

    def test_dot_release(self):
        self.assertEqual(compare_version_numbers('1.01', '1.001'), 1)
        self.assertEqual(compare_version_numbers('1.02', '1.2'), -1)


class FindPermutedStringsTest(unittest.TestCase):

    def test_find_none(self):
        occurrences = find_permuted_substring('abc', 'aaaabbbbbc')
        self.assertEqual(occurrences, [])

    def test_example(self):
        occurrences = find_permuted_substring(
            'abbc', 'cbabadcbbabbcbabaabccbabc')
        self.assertEqual(occurrences, [0, 6, 9, 11, 12, 20, 21])

    def test_repeats(self):
        occurrences = find_permuted_substring('bbc', 'bbbbbbbcbbc')
        self.assertEqual(occurrences, [5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
