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


def compare_version_numbers(v1, v2):
    """ https://leetcode.com/problems/compare-version-numbers/ """
    chunks1 = v1.split('.')
    chunks2 = v2.split('.')

    main1 = int(chunks1.pop(0))
    main2 = int(chunks2.pop(0))

    if main1 != main2:
        return (main1 - main2) / abs(main1 - main2)

    i = 0
    while i < len(chunks1) and i < len(chunks2):
        dr1 = chunks1[i]
        dr2 = chunks2[i]

        if len(dr1) == len(dr2):
            x = int(dr1)
            y = int(dr2)
            if x != y:
                return (x - y) / abs(x - y)
        else:
            if len(dr1) > len(dr2):
                x = int(dr1)
                y = int(dr2) * pow(10, len(dr1) - len(dr2))
            else:
                x = int(dr1) * pow(10, len(dr2) - len(dr1))
                y = int(dr2)
            if x != y:
                return (x - y) / abs(x - y)

        i += 1

    if len(chunks1) > len(chunks2):
        if sum(map(lambda x: int(x), chunks1[i:])) == 0:
            return 0
        return 1

    if len(chunks2) > len(chunks1):
        if sum(map(lambda x: int(x), chunks2[i:])) == 0:
            return 0
        return -1

    return 0


def find_permuted_substring(s, b):
    """Anagram substring search. Find all contiguous permutations of
    smaller string s in larger string b. Can be done in O(len(b)).

    """
    occurrences = []
    len_s = len(s)
    def char_to_index(c):
        return ord(c) - ord('a')

    counts_of_s = [0]*26
    for c in s:
        counts_of_s[char_to_index(c)] += 1

    counts_of_window = [0]*26
    i = 0
    while i < len(b):
        if i >= len_s:
            counts_of_window[char_to_index(b[i - len_s])] -= 1
        counts_of_window[char_to_index(b[i])] += 1
        if counts_of_s == counts_of_window:
            occurrences.append(i - len_s + 1)
        i += 1

    return occurrences


def compress_string(s):
    """aabcccccaaa => a2b1c5a3. If compressed string would not become
    smaller than the original string, just return original string.
    """
    compressed = ''
    i = 0
    while i < len(s):
        blockChar = s[i]
        count = 0
        while i < len(s) and s[i] == blockChar:
            count += 1
            i += 1

        compressed += blockChar + str(count)
        if len(compressed) >= len(s):
            return s

    return compressed
