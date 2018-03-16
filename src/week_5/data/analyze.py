import gensim


def main():

    # Loading the training data set
    from sklearn.datasets import fetch_20newsgroups

    # Choose only 4 categories out of the 20 available in the dataset
    categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']

    twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42,
                                      download_if_missing=False)

    # Look at the class names
    print("Class names: "+str(twenty_train.target_names))

    # How many documents/tweets there is in the training dataset
    print(""+len(twenty_train.data))

'''
sentences = [['first', 'sentence'], ['second', 'sentence']]

documents = [..]

# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)

# Observe words similarities
model.most_similar('thrump')
model.most_similar('obama')

model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
[('queen', 0.50882536)]
model.doesnt_match("breakfast cereal dinner lunch";.split())
'cereal'
model.similarity('woman', 'man')
0.73723527


# model

model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
model.build_vocab(some_sentences)  # can be a non-repeatable, 1-pass generator
model.train(other_sentences)  # can be a non-repeatable, 1-pass generator


# A reasonable value for min_count is between 0-100, depending on the size of your dataset.
model = Word2Vec(sentences, min_count=10)  # default value is 5

# size of the NN layers, which correspond to the degrees of freedom the training algorithm has
model = Word2Vec(sentences, size=200)  # default value is 100

# parallelization
model = Word2Vec(sentences, workers=4) # default = 1 worker = no parallelization

# evaluation
# test set
model.accuracy('/tmp/questions-words.txt')
#2014-02-01 22:14:28,387 : INFO : family: 88.9% (304/342)
#2014-02-01 22:29:24,006 : INFO : gram1-adjective-to-adverb: 32.4% (263/812)
#2014-02-01 22:36:26,528 : INFO : gram2-opposite: 50.3% (191/380)
#2014-02-01 23:00:52,406 : INFO : gram3-comparative: 91.7% (1222/1332)
#2014-02-01 23:13:48,243 : INFO : gram4-superlative: 87.9% (617/702)
#2014-02-01 23:29:52,268 : INFO : gram5-present-participle: 79.4% (691/870)
#2014-02-01 23:57:04,965 : INFO : gram7-past-tense: 67.1% (995/1482)
#2014-02-02 00:15:18,525 : INFO : gram8-plural: 89.6% (889/992)
#2014-02-02 00:28:18,140 : INFO : gram9-plural-verbs: 68.7% (482/702)
#2014-02-02 00:28:18,140 : INFO : total: 74.3% (5654/7614)


# If you need the raw output vectors in your application, you can access these either on a word-by-word basis
model['computer']  # raw NumPy vector of a word
array([-0.00449447, -0.00310097,  0.02421786, ...], dtype=float32)

'''

if __name__ == "__main__":
    main()