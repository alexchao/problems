# -*- coding: utf-8 -*-


def reverse_words(s):
    sentence = s.strip()
    space_index = sentence.find(' ', 0)
    if space_index < 0:
        return sentence
    return reverse_words(sentence[space_index + 1:]) + ' ' \
            + sentence[:space_index]
