from flask import Flask, render_template, request, url_for
from app import app
from app.dictionary import Dictionary
from app.edit_distance import EditDistance

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/handle_word', methods=['POST'])
def handle_word():
    unchecked_word = request.form['unchecked-word']
    # import pdb; pdb.set_trace()
    result = EditDistance.word_check(unchecked_word)
    return render_template('suggested.html', result=result)


@app.route('/word_list')
def word_list():
    return render_template('dictionary.html', events=len(Dictionary.read_txt()), dictionary_array=Dictionary.read_txt())
