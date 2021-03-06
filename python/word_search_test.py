# -*- coding: utf-8 -*-


import unittest


from word_search import CorpusIterator
from word_search import CorpusPosition
from word_search import find_pairs


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

    corpus_bookend = [
        'SHHHHS',
        'SHS',
        'SS'
    ]

    def test_empty_corpus(self):
        it = CorpusIterator([], 'A')
        self.assertFalse(it.has_next())
        self.assertIsNone(it.get_next())

    def test_basic(self):
        it = CorpusIterator(self.corpus, 'Y')
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(0, 24))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(2, 4))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(3, 1))
        self.assertFalse(it.has_next())
        self.assertIsNone(it.get_next())

    def test_bookend_occurrences(self):
        it = CorpusIterator(self.corpus_bookend, 'S')
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(0, 0))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(0, 5))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(1, 0))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(1, 2))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(2, 0))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(2, 1))
        self.assertFalse(it.has_next())
        self.assertIsNone(it.get_next())

    def test_only_get_next(self):
        it = CorpusIterator(self.corpus, 'X')
        self.assertEqual(it.get_next(), CorpusPosition(0, 23))
        self.assertEqual(it.get_next(), CorpusPosition(2, 3))
        self.assertEqual(it.get_next(), CorpusPosition(3, 0))

    def test_has_next_does_not_advance(self):
        it = CorpusIterator(self.corpus, 'X')
        self.assertEqual(it.get_next(), CorpusPosition(0, 23))
        it.has_next()
        it.has_next()
        it.has_next()
        self.assertEqual(it.get_next(), CorpusPosition(2, 3))

    def test_finds_consecutives(self):
        it = CorpusIterator(self.corpus_consecutive, 'D')
        self.assertEqual(it.get_next(), CorpusPosition(0, 3))
        self.assertEqual(it.get_next(), CorpusPosition(0, 4))
        self.assertEqual(it.get_next(), CorpusPosition(0, 5))
        self.assertEqual(it.get_next(), CorpusPosition(0, 6))
        self.assertEqual(it.get_next(), CorpusPosition(0, 7))
        self.assertEqual(it.get_next(), CorpusPosition(0, 12))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(1, 0))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(1, 1))
        self.assertFalse(it.has_next())

    def test_skip(self):
        it = CorpusIterator(self.corpus_consecutive, 'D')

        it.skip(CorpusPosition(0, 10))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(0, 12))

        it.skip(CorpusPosition(0, 1))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(0, 3))

        it.skip(CorpusPosition(1, 1))
        self.assertTrue(it.has_next())
        self.assertEqual(it.get_next(), CorpusPosition(1, 1))
        self.assertFalse(it.has_next())

    def test_skip_to_bad_position(self):
        it = CorpusIterator(self.corpus, 'A')
        with self.assertRaises(ValueError):
            it.skip(CorpusPosition(10, 0))

        with self.assertRaises(ValueError):
            it.skip(CorpusPosition(0, 100))

        with self.assertRaises(ValueError):
            it.skip(CorpusPosition(0, -1))


class FindPairsTest(unittest.TestCase):

    def test_find_none(self):
        self.assertEqual(find_pairs([], 'A', 'B'), [])
        self.assertEqual(find_pairs(['A'], 'A', 'B'), [])
        self.assertEqual(find_pairs(['B'], 'A', 'B'), [])
        self.assertEqual(find_pairs(['BA'], 'A', 'B'), [])
        self.assertEqual(find_pairs(['A', 'B'], 'A', 'B'), [])
        self.assertEqual(find_pairs(['B', 'A'], 'A', 'B'), [])

    def test_find_one(self):
        pairs = find_pairs(['XYZABXYZ'], 'A', 'B')
        self.assertEqual(pairs[0], CorpusPosition(0, 3))

    def test_two_in_a_row(self):
        pairs = find_pairs(['XYZABABXYZ'], 'A', 'B')
        self.assertEqual(pairs[0], CorpusPosition(0, 3))
        self.assertEqual(pairs[1], CorpusPosition(0, 5))

    def test_two_spaced_out(self):
        pairs = find_pairs(['XYZABJKLABXYZ'], 'A', 'B')
        self.assertEqual(pairs[0], CorpusPosition(0, 3))
        self.assertEqual(pairs[1], CorpusPosition(0, 8))

    def test_different_documents(self):
        pairs = find_pairs(['XYZABJKL', 'STUSTUABSTU'], 'A', 'B')
        self.assertEqual(pairs[0], CorpusPosition(0, 3))
        self.assertEqual(pairs[1], CorpusPosition(1, 6))

    def test_interleaved(self):
        pairs = find_pairs(['ABBAABBAAAXBXAB'], 'A', 'B')
        self.assertEqual(pairs[0], CorpusPosition(0, 0))
        self.assertEqual(pairs[1], CorpusPosition(0, 4))
        self.assertEqual(pairs[2], CorpusPosition(0, 13))

    def test_starts_with_second_token(self):
        pairs = find_pairs(['BAB'], 'A', 'B')
        self.assertEqual(pairs[0], CorpusPosition(0, 1))


if __name__ == '__main__':
    unittest.main()
