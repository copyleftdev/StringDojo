#!/usr/bin/env python

"""Top twenty sting interview question"""

import string
from itertools import permutations
from collections import OrderedDict

class StringDojo(object):
    """ Top 20 String Interview Questions """
    @classmethod
    def duplicate_characters_in_string(cls, strval):
        """ Find duplicate charaters in a string """
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in chars:
            count = strval.count(char)
            if count > 1:
                return char, count

    @classmethod
    def find_anagrams_in_string(cls, stringa, stringb):
        """find anagrams"""

        alist1 = list(stringa)
        alist2 = list(stringb)

        alist1.sort()
        alist1.sort()

        pos = 0
        matches = True

        while pos < len(stringa) and matches:
            if alist1[pos] == alist2[pos]:
                pos = pos + 1
            else:
                matches = False
        return matches

    @classmethod
    def find_non_repeated_chars(cls, strval):
        """find non repeating characters"""
        order = []
        counts = {}
        for char in strval:
            if counts:
                counts[char] += 1
            else:
                counts[char] += 1
                order.append(char)
        for char in order:
            if counts[char] == 1:
                return char
        return None

    @classmethod
    def recursively_reverse_string(cls, strval):
        """recursive string reversal"""
        if strval == "":
            return strval
        else:
            return strval[::-1]

    @classmethod
    def check_if_string_only_has_digits(cls, strval):
        """check for digits in string """
        for each_char in strval:
            if each_char.isdigit() == False:
                return False
            else:
                return True

    @classmethod
    def number_of_vowels_and_consonents(cls, strval):
        """return number of vowels and consoents"""
        vowels = list("aeiouy")
        consonants = list("bcdfghjklmnpqrstvxz")
        number_of_consonents = sum(strval.count(c) for c in consonants)
        number_of_vowels = sum(strval.count(c) for c in vowels)

        return number_of_vowels, number_of_consonents

    @classmethod
    def convert_numeric_string_to_int(cls, num_stings):
        """convert numberic string to integers"""
        num_list = []
        for char in num_stings:
            if char in string.letters or string.punctuation or string.whitespace:
                return None
            else:
                num_list.append(int(char))
        return num_list

    @classmethod
    def character_replacement(cls, strval, replacewith):
        """character replacement"""
        for char in strval:
            if char in replacewith:
                new_str = strval.replace(char, replacewith)
                return new_str
            else:
                return None

    @classmethod
    def find_all_permutations(cls, strtst):
        """Find all permutations in a string"""
        perms = [''.join(p)for p in permutations(strtst)]
        return perms

    @classmethod
    def check_for_palidrome(cls, strtst):
        """Check for palidrome in a string"""
        for i, char in enumerate(strtst):
            if char != strtst[-i-1]:
                return False
        return True

    @classmethod
    def remove_dupe_chars(cls, strtst):
        """remove duplicate characters from a string."""
        return "".join(OrderedDict.fromkeys(strtst))
