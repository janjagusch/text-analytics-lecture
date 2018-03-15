from lemmatization import tokenize

from sklearn.feature_extraction.text import TfidfVectorizer


def compute_tfidf(dataset):
    tfidf = TfidfVectorizer()
    idfs = tfidf.fit_transform(dataset)

    return tfidf, idfs


def compute_tfidf_stopwords(dataset, stopwords_lang):
    tfidf = TfidfVectorizer(stop_words=stopwords_lang)
    idfs = tfidf.fit_transform(dataset)

    return tfidf, idfs


def compute_tfidfle_stopwords(dataset, stopwords_lang):
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words=stopwords_lang)  # e.g. stop_words = 'english'
    idfs = tfidf.fit_transform(dataset)

    return tfidf, idfs