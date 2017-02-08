# -*- coding: utf-8 -*-
import unittest


from string_problems import reverse_words
from string_problems import group_anagrams
from string_problems import longest_substring


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
        assert longest_substring('abcabcbb') == 'abc'

    def test_no_repeats(self):
        assert longest_substring('abcdefgh') == 'abcdefgh'

    def test_repeated_character(self):
        assert longest_substring('bbbbb') == 'b'

    def test_continuation_of_repeated_character(self):
        assert longest_substring('pwwkew') == 'wke'

    def test_empty(self):
        assert longest_substring('') == ''

    def test_continguous(self):
        assert longest_substring('abcdaxyzb') == 'bcdaxyz'


if __name__ == '__main__':
    unittest.main()
