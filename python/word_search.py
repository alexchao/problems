# -*- coding: utf-8 -*-
from collections import namedtuple
import warnings


class CorpusPosition(namedtuple('CorpusPosition', ['document_id', 'index'])):

    def __str__(self):
        return 'CorpusPosition({0}, {1})'.format(self.document_id, self.index)

    def __repr__(self):
        return self.__str__()


class LazyCorpusIterator:
    """Iterates over occurrences of a given word in a corpus of `Document`s

    corpus -- list of `Document`s
    query -- word to iterate over

    """

    def __init__(self, corpus, query):
        self._corpus = corpus
        self._query = query
        self._next_search_pos = CorpusPosition(0, 0) if corpus else None
        self._has_staged = False
        self._staged_next = None

    def has_next(self):
        self._stage_next_if_needed()
        return bool(self._staged_next)

    def get_next(self):
        self._stage_next_if_needed()
        n = self._staged_next

        # advance search position
        self._next_search_pos = self._get_next_position(n) if n else None

        # unstage
        self._staged_next = None
        self._has_staged = False
        return n

    def skip(self, position):
        """Skip iterator to a desired CorpusPosition."""
        if not self._is_position_in_corpus(position):
            raise ValueError('{0} not in corpus'.format(position))

        self._staged_next = None
        self._has_staged = False
        self._next_search_pos = position

    def _stage_next_if_needed(self):
        if not self._staged_next and not self._has_staged:
            self._staged_next = self._get_next()
            self._has_staged = True

    def _get_next(self):
        if not self._next_search_pos:
            return None

        if not self._is_position_in_corpus(self._next_search_pos):
            warnings.warn('Starting search from a bad location: {0}'.format(
                self._next_search_pos))

        # use local variables since we don't want to permanently advance
        # the search position
        document_id = self._next_search_pos.document_id
        search_index = self._next_search_pos.index
        index = -1
        while index == -1 and self._is_document_in_corpus(document_id):
            index = self._find_query(
                self._query,
                self._corpus[document_id],
                search_index)

            if index == -1:
                # move on to the next document
                document_id += 1
                search_index = 0

        if index == -1:
            return None

        return CorpusPosition(document_id, index)

    def _is_position_in_corpus(self, p):
        if len(self._corpus) == 0:
            return False

        if not self._is_document_in_corpus(p.document_id):
            return False

        if p.index < 0:
            return False

        text = self._corpus[p.document_id]
        if p.index >= len(text):
            return False

        return True

    def _is_document_in_corpus(self, document_id):
        if not self._corpus:
            return False

        return 0 <= document_id and document_id < len(self._corpus)

    def _get_next_position(self, p):
        new_p = CorpusPosition(p.document_id, p.index + 1)
        if self._is_position_in_corpus(new_p):
            return new_p

        new_p = CorpusPosition(p.document_id + 1, 0)
        if self._is_position_in_corpus(new_p):
            return new_p

        return None


    @staticmethod
    def _find_query(query, text, start_index):
        return text.find(query, start_index)


class SimpleCorpusIterator:
    """Pre-process version of the iterator."""

    def __init__(self, corpus, query):
        self._elements = []
        self._pointer = -1

        for i, document in enumerate(corpus):
            search_position = 0
            while True:
                found_index = document.find(query, search_position)
                if found_index >= 0:
                    self._elements.append(CorpusPosition(i, found_index))
                    search_position = found_index + 1
                else:
                    break

        self._num_elements = len(self._elements)

    def has_next(self):
        return self._num_elements > 0 and self._pointer + 1 < self._num_elements

    def get_next(self):
        if not self.has_next():
            return None

        self._pointer += 1
        return self._elements[self._pointer]

    # This iterator's skip() method would be a bit trickier to implement.
    def skip(self, position):
        raise NotImplementedError()


CorpusIterator = LazyCorpusIterator


def find_pairs(corpus, a, b):
    """Find adjacent occurrences of a and b (with a necessarily preceding b)."""
    pairs = []
    it1 = CorpusIterator(corpus, a)
    it2 = CorpusIterator(corpus, b)

    def _is_pair(x, y):
        return x.document_id == y.document_id and x.index == y.index - 1

    def _cmp(x, y):
        if x.document_id == y.document_id:
            if x.index == y.index:
                return 0
            elif x.index > y.index:
                return 1
            else:
                return -1
        elif x.document_id > y.document_id:
            return 1
        else:
            return -1

    w1 = it1.get_next()
    w2 = it2.get_next()
    while w1 is not None and w2 is not None:
        cmp_value = _cmp(w1, w2)
        if cmp_value == -1:
            # w1 behind w2
            if _is_pair(w1, w2):
                pairs.append(w1)
                w1 = it1.get_next()
                w2 = it2.get_next()
            else:
                # TODO: what if this skip results in a bad position (e.g. -1)?
                it1.skip(CorpusPosition(w2.document_id, w2.index - 1))
                w1 = it1.get_next()
        elif cmp_value == 1:
            # w1 ahead of w2
            it2.skip(w1)
            w2 = it2.get_next()
        else:
            raise ValueError('Iterators are tracking same token')

    return pairs
