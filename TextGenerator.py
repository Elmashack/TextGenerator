import random
import nltk
import re

from collections import defaultdict
from nltk.tokenize import WhitespaceTokenizer

SENT_NUM = 10


def get_item_by_index(lst: list, ind: int):
    if not len(lst):
        return ""
    else:
        return lst[ind]


def main():
    tok = WhitespaceTokenizer()
    file_name = input("Enter the file name: ")
    with open(file_name, encoding='utf-8') as file:
        text = file.read()
    tokens = tok.tokenize(text)
    trigrams = tuple(nltk.trigrams(tokens))

    corpus = defaultdict(dict)
    for trigram in trigrams:
        head = f'{trigram[0]} {trigram[1]}'
        corpus[head].setdefault(trigram[2], 0)
        corpus[head][trigram[2]] += 1
    word = random.choice(tuple(corpus.keys()))
    for _ in range(SENT_NUM):
        sentence = []
        while True:
            if not len(sentence):
                # Generating first word in sentence
                next_word = ''.join(
                    random.choices(tuple(corpus[word].keys()), weights=tuple(corpus[word].values())))
                # Creating a head of trigrams for generating proper random word
                word = f'{word.split()[1]} {next_word}'
            else:
                next_word = ''.join(random.choices(tuple(corpus[word].keys()), weights=tuple(corpus[word].values())))
                # Creating a head of trigrams for generating proper random word
                word = f'{sentence[-1]} {next_word}'
            if re.match(r"[A-Za-z\d]+[.?!]+$", get_item_by_index(sentence, -1)) and len(sentence) >= 5:
                break
            # Check if it's a proper word for beginning of sentence
            elif re.match(r"[A-Z][a-z]+$", next_word) and \
                    (not sentence or re.match(r"[A-Za-z\d]+[.?!]+$", get_item_by_index(sentence, -1))):
                sentence.append(next_word)
            elif sentence:
                sentence.append(next_word)
        print(' '.join(sentence))

if __name__ == '__main__':
    main()
