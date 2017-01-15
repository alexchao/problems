# -*- coding: utf-8 -*-
import unittest


from string_problems import reverse_words


class ReverseWordsTest(unittest.TestCase):

    def test_reverse_sentence(self):
        assert reverse_words('it\'s not a tumor') == 'tumor a not it\'s'

    def test_reverse_word(self):
        assert reverse_words('bottle') == 'bottle'

    def test_reverse_empty(self):
        assert reverse_words('') == ''

    def test_reverse_whitespace(self):
        assert reverse_words(' alex chao ') == 'chao alex'


if __name__ == '__main__':
    unittest.main()
