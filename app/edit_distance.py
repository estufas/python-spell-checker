from flask import Flask, render_template, request, url_for
from app import app
from app.dictionary import Dictionary
from app.bi_search import BiSearch

class EditDistance:
    def word_check(unchecked_word):
        result = BiSearch.search(Dictionary.read_txt(), unchecked_word)
        if (result == False):
            possible_words = []
            for key, value in Dictionary.read_txt().items():
                result = EditDistance.levenshtein(unchecked_word, value)
                if (result < 2):
                    possible_words.append(value)
        return possible_words

    def levenshtein(source, target):
        if len(source) < len(target):
            return EditDistance.levenshtein(target, source)

        if len(target) == 0:
            return len(source)

        previous_row = range(len(target) + 1)
        for i, c1 in enumerate(source):
            current_row = [i + 1]
            for j, c2 in enumerate(target):
                insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1       # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]
