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

    tweets = load_tweets()

    russia_tweets = [tweet for tweet in tweets if 'russia' in tweet.text_cleaned]



if __name__ == '__main__':
    main()