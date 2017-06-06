from flask import Flask, render_template, request, url_for
from app import app

class Dictionary:
    def read_txt():
        with app.open_resource('static/usa.txt') as dictionary:
            dictionary_words = dictionary.read().splitlines()
            events = len(dictionary_words)
            dictionary_dict = {}
        for x in range(events):
            dictionary_dict[x] = dictionary_words[x].decode()
        return dictionary_dict
