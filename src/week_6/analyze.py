from src.week_6.features.normalize_corpus import corpus_w2v
from src.week_6.models import collocations, word2vec

"""
    Lets look at the implementation of Collocations for Bigrams
"""

# Load and normalize the dataset
norm_alice = collocations.load_alice_corpus()

# Top 10 bigrams by frequency
print(collocations.get_top_ngrams(corpus=norm_alice, ngram_val=2, limit=10))


# Top 10 trigrams by frequency
print(collocations.get_top_ngrams(corpus=norm_alice, ngram_val=3, limit=10))


""" BLOCK 1 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

finder, bigram_measures = collocations.compute_collocation_bigram(norm_alice)

top10_freq_bigram_collocations = collocations.get_top_collocations_freq(finder, bigram_measures, 10)

print(top10_freq_bigram_collocations)

"""  # BLOCK 1 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

"""  BLOCK 2 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK
top10_pmi_bigram_collocations = collocations.get_top_collocations_pmi(finder, bigram_measures, 10)

print(top10_pmi_bigram_collocations)

"""  # BLOCK 2 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

#   QUESTIONS:
#   Q1. What is the difference between function collocations.get_top_ngrams and collocations.get_top_collocations_freq?
#   Q2. Why is the TOP10 from the function top10_freq_bigram_collocations different from top10_pmi_bigram_collocations?


"""
    Lets look at word vectors (Word2Vec)
"""
"""  # BLOCK 3 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK
corpus_w2v = corpus_w2v(norm_alice)
w2v = word2vec.compute_word2vec(corpus=corpus_w2v, size=10, min_count=2)

w2v_vocabulary = w2v.wv.vocab
print('w2v Vocabulary: '+str(w2v_vocabulary))

size_w2v_vocabulary = len(w2v.wv.vocab)
print('w2v Vocabulary size: '+str(size_w2v_vocabulary))

"""  # BLOCK 3 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

"""  # BLOCK 4 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

alice_word_vector = w2v['alice']
print('Word vector for the word \'alice\':\n'+str(w2v['alice']))

"""  # BLOCK 4 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

"""  # BLOCK 5 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

most_similar_terms = w2v.most_similar('alice')
print('According to w2v model which are the terms most similar to the word \'alice\':\n+'+str(most_similar_terms))

most_similar_terms = w2v.most_similar('agony')
print('According to w2v model which are the terms most similar to the word \'agony\':\n+'+str(most_similar_terms))

terms_similarity = w2v.similarity('alice', 'rabbit')
print('Similarity between word \'alice\' and word \'rabbit\':'+str(terms_similarity))

terms_similarity = w2v.similarity('alice', 'king')
print('Similarity between word \'alice\' and word \'king\':'+str(terms_similarity))

terms_similarity = w2v.similarity('thump', 'king')
print('Similarity between word \'thump\' and word \'king\':'+str(terms_similarity))

"""  # BLOCK 5 - DELETE THIS LINE AFTER THE PREVIOUS CODE WAS OK

#   QUESTIONS:
#   Q1. Change the size of the dimensions from 10 to 100000
#   Q2. Look at the terms similarities. Are they the same? YES/NO. Why do you think that happen?

