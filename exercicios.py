import nltk
#nltk.download()
from nltk.corpus import gutenberg
from random import choice
from nltk.corpus import udhr
from nltk.corpus import brown
from nltk.corpus import swadesh
from nltk.corpus import names
from nltk.corpus import wordnet
from nltk.corpus import words
import re
from collections import defaultdict


'''
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
print('\nExercicio 2.1')
freq10 = []
palavras = nltk.FreqDist(brown.words())
for palavra in palavras:
    if palavras[palavra] >= 10000:
        freq10.append(palavra)
print(freq10)
print('\nExercicio 2.2')
swadesh.fileids()
texto = swadesh.raw('pt')
letras = []
for letra in texto:
    letra_freq = [letra, nltk.FreqDist(texto)[letra]]
    letras.append(letra_freq)
print(letras)
print('\nExercicio 3.1')
letra_freq = nltk.ConditionalFreqDist()
for lingua in swadesh.fileids():
    for letra in swadesh.raw(lingua).lower():
        if letra.isalpha():
            letra_freq[lingua][letra] +=1
letra_freq.tabulate(samples='abcdefghijklmnopqrstuvwxyz')
print('\nExercicio 3.2')
letra_freq = nltk.ConditionalFreqDist()
for genero in names.fileids():
    for nome in names.words(genero):
        letra_freq[genero][nome[0]] +=1
letra_freq.tabulate(samples='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('\nExercicio 3.3')
for categoria in brown.categories():
    diversidade = len(brown.words(categories=[categoria])) / len(set(brown.words(categories=[categoria])))
    print(categoria,diversidade)
print('\nExercicio 8.1')
substantivos = 0
nao_hyponymys = 0
for palavra in wordnet.all_synsets('n'):
    substantivos +=1
    if palavra.hyponyms():
        nao_hyponymys +=1
print(nao_hyponymys/substantivos)
print('\nExercicio 8.2')
total = 0
quantidade = 0
for palavra in wordnet.all_synsets('n'):
    total += len(palavra.hyponyms())
    quantidade +=1
print(total/quantidade)
print('\nExercicio 10.1')
palavras = ['music', 'dog', 'parrot']
synset_word = []
synset_table = []
for palavra in palavras:
    for synset in wordnet.synsets(palavra, 'n'):
        synset_word.append(synset)
for i, synset1 in enumerate(synset_word):
    synset_path = []
    synset_path.append(synset1)
    for synset2 in synset_word:
        synset_path.append('{:3.1f}'.format(synset1.path_similarity(synset2)*100))
    synset_table.append(synset_path)
for synset in synset_table:
    print(synset)
print('\nExercicio 11.1')
print('*ed')
for word in nltk.corpus.words.words('en'):
    if re.search('ed$', word):
        print(word)
print('\n**j**t**')
for word in nltk.corpus.words.words('en'):
    if re.search('^..j..t..$', word):
        print(word)   
print('\n[ghi][mno][jlk][def]')
for word in nltk.corpus.words.words('en'):
    if re.search('^[ghi][mno][jlk][def]$', word):
        print(word)
print('\nExercicio 11.2')
print('[0-9]')
for word in nltk.corpus.treebank.words():
    if re.search('[0-9]', word):
        print(word)
print('\n[0-9]*4')
for word in nltk.corpus.treebank.words():
    if re.search('^[0-9]{4}$', word):
        print(word)
print('\n[0-9]*4 inteiros')
for word in nltk.corpus.treebank.words():
    if re.search('^[0-9]{4,}$', word):
        print(word)
print('\n[0-9] decimais')
for word in nltk.corpus.treebank.words():
    if re.search('^[0-9]+\.[0-9]+$', word):
        print(word)
print('\n*ed ou *ing')
for word in nltk.corpus.treebank.words():
    if re.search('(ed|ing)$', word):
        print(word)
print('\npalavras compostas')
for word in nltk.corpus.treebank.words():
    #if re.search('^[a-z]+-[a-z]+$', word):
        #print(word)
    if re.search('^[a-z]+-[a-z]+-[a-z]+$', word):
        print(word)
print('\nExercicio 12.1')
frequencia = []
duas_vogais = []
palavras = []
for palavra in nltk.corpus.treebank.words():
    palavras.append(palavra)
palavras = set(palavras)
for palavra in palavras:
    for vogais in (re.findall(r'[aeiou]{2,}', palavra)):
        duas_vogais.append(vogais)
for vogais in duas_vogais:
    frequencia_vogal = [vogais, nltk.FreqDist(duas_vogais)[vogais]]
    if not(frequencia_vogal in frequencia):
        frequencia.append(frequencia_vogal)
print(frequencia)
print('\nExercicio 12.2')
pares = []
mapping = defaultdict(list)
silabas = []
for palavra in nltk.corpus.toolbox.words('rotokas.dic'):
    for silaba in re.findall(r'[bcdfghjklmnpqrstvxz][aeiou]', palavra):
        silabas.append(silaba)
        mapping[silaba].append(palavra)
        pares.append((silaba,palavra))
frequencia = nltk.ConditionalFreqDist(silabas)
print("tabela de silabas cons + vog")
frequencia.tabulate()
print(mapping['te'])
sumarizado = nltk.Index(pares)
print(sumarizado['te'])
print('\nExercicio 13 PERGUNTAR')
texto = """
DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government. Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony.
"""
tokens = nltk.word_tokenize(texto)
palavras = []
porter = nltk.PorterStemmer()
for palavra in tokens:
    if re.findall((r'^(.*?)(ing|ed|yng)?$'), palavra):
        palavras.append(palavra)
        porter.stem(palavra)
print(palavras)
print(porter)
'''
print('\nExercicio 14')
print(nltk.Text(nltk.corpus.brown.words()).findall(r"<\w*> <and> <other> <\w*s>"))
