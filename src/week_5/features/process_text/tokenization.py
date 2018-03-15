from sklearn.feature_extraction.text import CountVectorizer


def word_tokenize(dataset):
    """
    Previous class tokenization was done using ntlk. In this class we learn how to do it with scikit-learn
    Args:
        dataset: a collection of documents stored in a vector
    Returns:
        A list of words, corresponding to the indexed vocabulary of the dataset
    """
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(dataset)

    return x, vectorizer


def ngrams_tokenize(dataset, range_begin, range_end):
    """
    Previous class tokenization was done using ntlk. In this class we learn how to do it with scikit-learn
    Args:
        dataset: a collection of documents stored in a vector
    Returns:
        A list of ngrams, corresponding to the indexed vocabulary of the dataset
    """
    ngram_vectorizer = CountVectorizer(ngram_range=(range_begin, range_end), token_pattern=r'\b\w+\b', min_df=1)
    x = ngram_vectorizer.fit_transform(dataset)

    return x, ngram_vectorizer


def vocabulary_size(vectorizer):
    return len(vectorizer.get_feature_names())