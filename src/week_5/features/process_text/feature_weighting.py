<<<<<<< HEAD
from week_5.features.process_text.lemmatization import tokenize
=======
from src.week_5.features.process_text.lemmatization import tokenize

>>>>>>> 53b9dcf6fd57cc9ae9b4ed7e9488e48139b53f84
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