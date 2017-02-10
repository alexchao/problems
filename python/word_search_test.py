# -*- coding: utf-8 -*-


import unittest


from word_search import CorpusIterator
from word_search import CorpusPosition


def assert_equal_position(p1, p2):
    assert p1 is not None and p2 is not None
    assert (p1.document_id == p2.document_id and p1.index == p2.index), \
            '{0} != {1}'.format(p1, p2)


class CorpusIteratorTest(unittest.TestCase):

    corpus = [
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'ABC',
        'ABCXYZ',
        'XYZ'
    ]

    corpus_consecutive = [
        'ABCDDDDDEFGHD',
        'DD'
    ]

    def test_basic(self):
        it = CorpusIterator(self.corpus, 'Y')
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(0, 24))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(2, 4))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(3, 1))
        assert not it.has_next()
        assert it.get_next() is None

    def test_only_get_next(self):
        it = CorpusIterator(self.corpus, 'X')
        assert_equal_position(it.get_next(), CorpusPosition(0, 23))
        assert_equal_position(it.get_next(), CorpusPosition(2, 3))
        assert_equal_position(it.get_next(), CorpusPosition(3, 0))

    def test_has_next_does_not_advance(self):
        it = CorpusIterator(self.corpus, 'X')
        assert_equal_position(it.get_next(), CorpusPosition(0, 23))
        it.has_next()
        it.has_next()
        it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(2, 3))

    def test_finds_consecutives(self):
        it = CorpusIterator(self.corpus_consecutive, 'D')
        assert_equal_position(it.get_next(), CorpusPosition(0, 3))
        assert_equal_position(it.get_next(), CorpusPosition(0, 4))
        assert_equal_position(it.get_next(), CorpusPosition(0, 5))
        assert_equal_position(it.get_next(), CorpusPosition(0, 6))
        assert_equal_position(it.get_next(), CorpusPosition(0, 7))
        assert_equal_position(it.get_next(), CorpusPosition(0, 12))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(1, 0))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(1, 1))
        assert not it.has_next()

    def test_skip(self):
        it = CorpusIterator(self.corpus_consecutive, 'D')

        it.skip(CorpusPosition(0, 10))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(0, 12))

        it.skip(CorpusPosition(0, 1))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(0, 3))

        it.skip(CorpusPosition(1, 1))
        assert it.has_next()
        assert_equal_position(it.get_next(), CorpusPosition(1, 1))
        assert not it.has_next()



if __name__ == '__main__':
    unittest.main()
