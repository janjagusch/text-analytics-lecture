from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wordnet.ADJ
    elif is_noun(tag):
        return wordnet.NOUN
    elif is_adverb(tag):
        return wordnet.ADV
    elif is_verb(tag):
        return wordnet.VERB
    return None


def lemma_tokens(tokens, wnl):
    lemmas = []
    for item in tokens:
        pos = pos_tag([item])[0][1]
        ptw = penn_to_wn(pos)
        if ptw is None:
            lemmas.append(wnl.lemmatize(item))
        else:
            lemmas.append(wnl.lemmatize(item, ptw))
    return lemmas


def tokenize(text):
    wnl = WordNetLemmatizer()

    tokens = word_tokenize(text)
    lemmas = lemma_tokens(tokens, wnl)

    return lemmas


def lemmatization(dataset):
    dataset_lemma = list()
    for doc in dataset:
        doc_lemmas = tokenize(doc)
        c_doc = ''
        for token in doc_lemmas:
            c_doc += token + ' '
        dataset_lemma.append(c_doc.strip())
    return dataset_lemma