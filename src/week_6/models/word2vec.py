from gensim.models import Word2Vec


def compute_word2vec(corpus, size, min_count):
    """
    Args:
    corpus: a collection of documents stored in a vector. For example:
    [['this', 'is', 'just', 'a', 'random', 'sample'], ['second', 'sentence', 'to', 'test', 'sample']

    size: is dimensions size (e.g. 10 from Text Classification class)

    min_count: minimum frequency of each term in the vocabulary

    Returns:
    word2vec model
    """
    model = Word2Vec(corpus, size=size, min_count=min_count)

    return model


