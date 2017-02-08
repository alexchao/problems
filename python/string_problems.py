# -*- coding: utf-8 -*-


def reverse_words(s):
    sentence = s.strip()
    space_index = sentence.find(' ', 0)
    if space_index < 0:
        return sentence
    return reverse_words(sentence[space_index + 1:]) + ' ' \
            + sentence[:space_index]


def group_anagrams(list_of_words):

    def _word_to_id(w):
        word_lower = w.lower()
        sorted_chars = sorted(word_lower, key=ord)
        return ''.join(sorted_chars)

    id_to_words = {}
    for word in list_of_words:
        word_id = _word_to_id(word)
        if word_id not in id_to_words:
            id_to_words[word_id] = [word]
        else:
            id_to_words[word_id].append(word)

    return [set(v) for k, v in id_to_words.items()]


def longest_substring(s):
    start = max_length = 0
    char_last_index = {}
    for i, char in enumerate(s):
        if char in char_last_index and start <= char_last_index[char]:
            start = char_last_index[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        char_last_index[char] = i
    return max_length
