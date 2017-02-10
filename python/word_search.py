# -*- coding: utf-8 -*-
from collections import namedtuple


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
        self._current_document_id = 0
        self._current_query_index = 0
        self._has_staged = False
        self._staged_next = None

    def has_next(self):
        self._stage_next_if_needed()
        return bool(self._staged_next)

    def get_next(self):
        self._stage_next_if_needed()
        n = self._staged_next
        if n is not None:
            # advance
            self._current_document_id = n.document_id
            self._current_query_index = n.index + 1
        # unstage
        self._staged_next = None
        self._has_staged = False
        return n

    def _stage_next_if_needed(self):
        if not self._staged_next and not self._has_staged:
            self._staged_next = self._get_next()
            self._has_staged = True

    def _get_next(self):
        document_id = self._current_document_id
        search_index = self._current_query_index
        index = -1
        while index == -1 and 0 <= document_id and document_id < len(self._corpus):
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


CorpusIterator = LazyCorpusIterator
