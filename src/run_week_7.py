from builtins import dict

from week_7.data.io import load_tweets
import itertools
import math
import pandas
import collections
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD, LatentDirichletAllocation
from numpy.random import choice
from gensim import corpora, models



def main():

    # Term-Frequency-Inverse-Document-Frequency (TF-IDF).
    print('Term-Frequency-Inverse-Document-Frequeny (TF-IDF)')

    # Create two documents.
    docs = ['the dog sits on the table',
            'the cat sits on the sofa']
    docs_counter = [collections.Counter(doc.split()) for doc in docs]

    # Create unique term set.
    terms = set(itertools.chain.from_iterable(docs_counter))

    # Create term-frequency function.
    def tf(t, d):
        """Calculates term-frequency for term t in document d."""

        # If term in document, return frequency. Else, return null:
        if t in d.keys():
            return d[t]
        else:
            return 0

    # Calculate term-frequency matrix.
    tf_matrix = [{t:tf(t, d) for t in terms} for d in docs_counter]

    # Create inverse document-frequency function.
    def idf(t, D):
        """Calculates inverse document-frequency for term t in documents D."""
        return math.log(len(D) / len([d for d in D if t in d.keys()]),2)

    # Calculate inverse document-frequency vector.
    idf_vector = {t: idf(t, docs_counter) for t in terms}

    # Calculate term-frequency inverse document-frequency matrix.
    tfidf_matrix = [{t: tf_vector[t]*idf_vector[t] for t in terms} for tf_vector in tf_matrix]

    # Label term-frequency columns.
    tf_cols = ['tf_' + str(i + 1) for i in range(len(tf_matrix))]

    # Labels term-frequency inverse-document-frequency columns.
    tfidf_cols = ['tfidf_' + str(i + 1) for i in range(len(tfidf_matrix))]

    # Create function to build pandas data frame.
    def create_df(tf_matrix, idf_vector, tfidf_matrix, tf_cols, tfidf_cols):
        # Create data frame dictionary.
        df_dict = {}

        # Fill data frame dictionary.
        for tf_col, tf_vector in zip(tf_cols, tf_matrix): df_dict[tf_col] = tf_vector
        df_dict['idf'] = idf_vector
        for tfidf_col, tfidf_vector in zip(tfidf_cols, tfidf_matrix): df_dict[tfidf_col] = tfidf_vector

        # Create column order.
        col_order = []
        col_order.extend(tf_cols)
        col_order.append('idf')
        col_order.extend(tfidf_cols)

        # Create data frame and order by column order.
        df = pandas.DataFrame.from_dict(df_dict)
        df = df[col_order]

        return df

    # Print data frame.
    print('\n\nStandard TF-IDF\n')
    print(create_df(tf_matrix, idf_vector, tfidf_matrix, tf_cols, tfidf_cols))

    # Advanced TF-IDF techniques.

    # Sub-linear term-frequency.
    def tf(t, d, sub_linear=False):
        """Calculates term-frequency for term t in document d."""

        # If term in document, return frequency. Else, return null:
        if t in d.keys():
            # If sub_linear, return log of tf.
            if sub_linear:
                return math.log(d[t]) + 1
            else:
                return d[t]
        else:
            return 0

    print('\n\nSub-Linear TF-IDF\n')
    tf_matrix = [{t:tf(t, d, sub_linear=True) for t in terms} for d in docs_counter]
    tfidf_matrix = [{t: tf_vector[t] * idf_vector[t] for t in terms} for tf_vector in tf_matrix]
    print(create_df(tf_matrix, idf_vector, tfidf_matrix, tf_cols, tfidf_cols))

    # Smoother for inverse document-frequency.
    def idf(t, D, smoother=False):
        """Calculates inverse document-frequency for term t in documents D."""

        val = len(D) / len([d for d in D if t in d.keys()])

        # If smoother, add 1 to val
        if smoother:
            val += 1
        return math.log(val, 2)

    print('\n\nSmoother TF-IDF\n')
    idf_vector = {t: idf(t, docs_counter, True) for t in terms}
    tfidf_matrix = [{t: tf_vector[t] * idf_vector[t] for t in terms} for tf_vector in tf_matrix]
    print(create_df(tf_matrix, idf_vector, tfidf_matrix, tf_cols, tfidf_cols))

    # Normalizing term-frequency.
    def tf(t, d, sub_linear=False, normalization=None):
        """Calculates term-frequency for term t in document d."""

        # If normalization is in ['l1', 'l2'], apply normalization.
        if normalization in ['l1', 'l2']:
            # If normalization is 'l1', apply l1 normalization.
            if normalization == 'l1':
                normalizer = numpy.sum(numpy.abs(list(d.values())))
            # If normalization is 'l2', apply l2 normalization.
            if normalization == 'l2':
                normalizer = numpy.sqrt(numpy.sum(numpy.square(list(d.values()))))
            d_norm = {word: d[word] / normalizer for word in d.keys()}
        else:
            d_norm = d

        # If term in document, return frequency. Else, return null:
        if t in d_norm.keys():
            # If sub_linear, return log of tf.
            if sub_linear:
                return math.log(d_norm[t])
            else:
                return d_norm[t]
        else:
            return 0

    print('\n\nL1 TF-IDF\n')
    tf_matrix = [{t:tf(t, d, False, 'l1') for t in terms} for d in docs_counter]
    tfidf_matrix = [{t: tf_vector[t] * idf_vector[t] for t in terms} for tf_vector in tf_matrix]
    print(create_df(tf_matrix, idf_vector, tfidf_matrix, tf_cols, tfidf_cols))

    print('\n\nL2 TF-IDF\n')
    tf_matrix = [{t:tf(t, d, False, 'l2') for t in terms} for d in docs_counter]
    idf_vector = {t: idf(t, docs_counter) for t in terms}
    tfidf_matrix = [{t: tf_vector[t] * idf_vector[t] for t in terms} for tf_vector in tf_matrix]
    print(create_df(tf_matrix, idf_vector, tfidf_matrix, tf_cols, tfidf_cols))

    # TF-IDF with scikit-learn.
    def tfidf_extractor(corpus, ngram_range=(1, 1)):

        vectorizer = TfidfVectorizer(min_df=1,
                                     norm='l2',
                                     smooth_idf=False,
                                     use_idf=True,
                                     ngram_range=ngram_range)
        features = vectorizer.fit_transform(corpus)
        return vectorizer, features

    tfidf_vectorizer, tfidf_features = tfidf_extractor(docs)

    print('\n\nScikit-Learn TF-IDF\n')
    print(pandas.DataFrame(data=tfidf_features.todense(), columns=tfidf_vectorizer.get_feature_names()).T)

    # Singular Value Decomposition.

    movie_dict = {'matrix': [1, 3, 4, 5, 0, 0, 0],
                    'alien': [1, 3, 4, 5, 2, 0, 1],
                    'serenity': [1, 3, 4, 5, 0, 0, 0],
                    'casablanca': [0, 0, 0, 0, 4, 5, 2],
                    'amelie': [0, 0, 0, 0, 4, 5, 2]}

    movie_matrix = pandas.DataFrame.from_dict(movie_dict)

    print('\n\nOriginal Matrix\n')
    print(movie_matrix)

    svd_model = TruncatedSVD(n_components=2)
    svd_features = svd_model.fit_transform(movie_matrix)

    print('\n\nSVD Features\n')
    print(pandas.DataFrame(svd_features))

    print('\n\nSVD Singular Values\n')
    print(pandas.DataFrame(svd_model.singular_values_))

    print('\n\nSVD Components\n')
    print(pandas.DataFrame(svd_model.components_))

    # Latent Semantic Indexing.

    dictionary = corpora.Dictionary([d.split() for d in docs])
    print(dictionary.token2id)

    corpus = [dictionary.doc2bow(text) for text in [d.split() for d in docs]]
    corpus

    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    total_topics = 2

    lsi = models.LsiModel(corpus_tfidf,
                          id2word=dictionary,
                          num_topics=total_topics)

    pandas.DataFrame(lsi.print_topics(total_topics))

    df = pandas.DataFrame(lsi.projection.u)
    df['term'] = lsi.id2word.id2token.values()
    df = df.set_index('term')


    # Latent Dirichlet Allocation.

    lda_model = LatentDirichletAllocation(n_components=2, doc_topic_prior=0.1, topic_word_prior=0.1)
    lda_features = lda_model.fit_transform(movie_matrix)

    print('\n\nLDA Features\n')
    print(pandas.DataFrame(lda_features))

    print('\n\nLDA Components\n')
    print(pandas.DataFrame(lda_model.exp_dirichlet_component_))

    # Example based on real Trump tweets.
    tweets = load_tweets()

    cleaned_tweets = [list(itertools.chain.from_iterable(d.text_cleaned)) for d in tweets if d.text_cleaned is not None]

    china_tweets = choice([t for t in cleaned_tweets if 'china' in t], 50)
    mexico_tweets = choice([t for t in cleaned_tweets if 'mexico' in t], 50)
    russia_tweets = choice([t for t in cleaned_tweets if 'russia' in t], 50)

    sample_tweets = list()
    sample_tweets.extend(china_tweets)
    sample_tweets.extend(mexico_tweets)
    sample_tweets.extend(russia_tweets)

    sample_tweets = [' '.join(s) for s in sample_tweets]

    tfidf_matrix = tfidf_vectorizer.fit_transform(sample_tweets)

    lda_model = LatentDirichletAllocation(n_components=3, doc_topic_prior=0.5, topic_word_prior=0.5)
    lda_features = lda_model.fit_transform(tfidf_matrix)

    print(1)






if __name__ == '__main__':
    main()