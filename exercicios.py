import nltk
from nltk.corpus import gutenberg
from random import choice
from nltk.corpus import udhr

print('\nExercicio 1.1')
texto = gutenberg.words('austen-persuasion.txt')
print('austen-persuasion.txt possui ' + str(len(texto)) + ' palavras')
print('são apenas ' + str(len(set(texto))) + ' diferentes')

print('\nExercicio 1.2')
texto = []
for palavra in gutenberg.words():
    if palavra.isalpha():
        texto.append(palavra.lower())

trigrams = nltk.trigrams(texto)
sentenca = []
i = 0
for a, b, c in trigrams:
    i+=1
    sentenca.append(choice([a,b,c]))
    if i == 20:
        break

print(" ".join(sentenca))

#nao entendi
print('\nExercicio 1.3')
def find_language(palavra):
    linguas = []
    for lingua in udhr.fileids():
        if lingua.endswith('Latin1') and palavra in nltk.corpus.udhr.words(lingua):
            linguas.append(lingua)
    return linguas

print(find_language('one'))
print(find_language('ein'))
print(find_language('gar'))
