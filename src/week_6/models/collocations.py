'''
This example was taken from:
Text Analytics with Python: A Practical Real-World Approach to Gaining Actionable Insights from Your Data,
By Dipanjan Sarkar
Chapter 5: Text Summarization
'''

import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import gutenberg
from operator import itemgetter
from src.week_6.features.normalize_corpus import normalize_corpus
from copy import deepcopy


def load_alice_corpus():
    # load corpus
    alice = gutenberg.sents(fileids='carroll-alice.txt')
    alice = [' '.join(ts) for ts in alice]

    #norm_alice = filter(None, normalize_corpus(alice, tokenize=False))
    norm_alice = normalize_corpus(alice, tokenize=False)

    # print first line
    #print(alice[0])  # alice adventures wonderland lewis carroll 1865

    return norm_alice


def flatten_corpus(corpus):
    return ' '.join([document.strip() for document in corpus])


def compute_ngrams(sequence, n):
    return zip(*[sequence[index:] for index in range(n)])


def get_top_ngrams(corpus, ngram_val=1, limit=5):
    c_corpus = deepcopy(corpus)
    c_corpus = flatten_corpus(c_corpus)
    tokens = nltk.word_tokenize(c_corpus)
    ngrams = compute_ngrams(tokens, ngram_val)
    ngrams_freq_dist = nltk.FreqDist(ngrams)
    sorted_ngrams_fd = sorted(ngrams_freq_dist.items(),
                              key=itemgetter(1), reverse=True)
    sorted_ngrams = sorted_ngrams_fd[0:limit]
    sorted_ngrams = [(' '.join(text), freq)
                     for text, freq in sorted_ngrams]
    return sorted_ngrams


def compute_collocation_bigram(corpus):
    finder = BigramCollocationFinder.from_documents([item.split() for item in corpus])
    bigram_measures = BigramAssocMeasures()

    return finder, bigram_measures


def get_top_collocations_freq(finder, bigram_measures, top):
    return finder.nbest(bigram_measures.raw_freq, top)

def get_top_collocations_pmi(finder, bigram_measures, top):
    return finder.nbest(bigram_measures.pmi, top)


#norm_alice = load_alice_corpus()

# top 10 bigrams
#print(get_top_ngrams(corpus=norm_alice, ngram_val=2, limit=10))


# top 10 tuigrams
#print(get_top_ngrams(corpus=norm_alice, ngram_val=3, limit=10))