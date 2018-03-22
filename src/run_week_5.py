import week_5.data.look_at_data as dt
from week_5.evaluation import metrics
from week_5.features.process_text.tokenization import word_tokenize, ngrams_tokenize, vocabulary_size
from week_5.features.process_text.feature_weighting import compute_tfidf, compute_tfidf_stopwords, \
    compute_tfidfle_stopwords
from week_5.models.supervised_classification import multinomial_naive_bayes, look_at_predictions, prediction
from week_5.utils.look_tfidfs import look_at_features

def main():
    """
    The objective of this class is to investigate different techniques to:
        1. Use sklearn to explore data
        2. Lemmatization with sklearn
        3. TF-IDF
        4. Supervised learning
        5. Evaluation metrics
    """

    """
    SECTION #1:
    Learn how our data is structured
    """

    # # The selection of categories is optional. If empty we will obtain samples from all categories
    # # subset can be: train, test or all
    # news_train = dt.load_dataset('train')
    #
    # # Classes in the dataset.
    # target_classes = dt.target_classes(news_train)
    # print('Classes in the dataset: '+str(target_classes))
    #
    # # Number of training samples:
    # nr_training_samples = dt.nr_samples(news_train)
    # print('Number of training samples: '+str(nr_training_samples))
    #
    # print("\nLook at the information of a sample stored in position 5 (this is just an example you can try others)\n")
    # sample_pos = 5
    # class_pos = dt.sample_class_pos(news_train, sample_pos)
    # print('News article class number: '+str(class_pos))
    # print('News article class: '+str(dt.sample_class(news_train, class_pos)))
    # print('News article filename: '+str(dt.sample_filename(news_train, sample_pos)))
    #
    # news = dt.sample_content(news_train, sample_pos)
    # print('News article content: \n'+news)

    """
    SECTION #2:
        Look at an example were we do BOW and n-grams(=2)
            2.1 Use the function from features.process_text.lemmatization to compute lemmas from the dataset
                a) Look at data (similar to point 2)
            2.2. Compare the vocabulary size with and without using lemmas.
                a) Is it the same as before we applied the lemmas? Yes/No what happen?
    """

    # # Tokenization (BOW)
    # bow_index, bow_vectorizer = word_tokenize(news_train.data)  # data.data = data_lst.tolist()
    #
    # # Vocabulary size
    # print('Vocabulary size (bow): '+str(vocabulary_size(bow_vectorizer)))
    #
    # # Look at some of the vocabulary
    # print(bow_vectorizer.get_feature_names()[10000:10010])
    #
    # # Try an example
    # bow_analyze = bow_vectorizer.build_analyzer()
    # bow_sample = bow_analyze('Working with text is super cool!')
    # print('BOW sample: '+str(bow_sample))
    #
    # # Tokenization (bigrams)
    # bigram_index, bigram_vectorizer = ngrams_tokenize(news_train.data, 1, 2)
    #
    # # Vocabulary size
    # print('Vocabulary size (bigrams): '+str(vocabulary_size(bigram_vectorizer)))
    # perc = round(float(vocabulary_size(bigram_vectorizer)*100)/vocabulary_size(bow_vectorizer), 2)
    # print('Bigrams vocabulary size is '+str(perc)+'% larger than bow')
    #
    # # Look at some of the vocabulary
    # print(bigram_vectorizer.get_feature_names()[200000:200010])

    """
    SECTION #3:
        TF-IDF
            3.1 Look at the functions: tfidf, tfidf_lemma_stopwords (week_5.features.process_text.feature_weighting)
            3.2 Run the bellow code. Notice that if we use stopwords or lemmatization TFIDF weights change. Why is that?
    WARNING: THIS SECTION CAN TAKE A LONG TIME TO COMPUTE!
    """

    # tfidf, idfs = compute_tfidf(news_train.data)
    #
    # tfidf_sw, idfs_sw = compute_tfidf_stopwords(news_train.data, stopwords_lang='english')
    #
    # tfidfle_sw, idfsle_sw = compute_tfidfle_stopwords(news_train.data, stopwords_lang='english')
    #
    # sentence = 'Kingdom of Heaven is a 2005 epic historical drama film directed and produced ' \
    #            'by Ridley Scott and written by William Monahan.'
    #
    # response = tfidf.transform([sentence])
    # look_at_features(tfidf, response)
    #
    # response = tfidf_sw.transform([sentence])
    # look_at_features(tfidf_sw, response)
    #
    # response = tfidfle_sw.transform([sentence])
    # look_at_features(tfidfle_sw, response)

    """
    SECTION #4:
        Supervised learning
            4.1 Compute the Multinominal Naive Bayes for BOW, Bigrams and TFIDF (with lemmas and stopwords)
            4.2 Implement SVM (TIP: http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
    """

    # tfidf, idfs = compute_tfidf(news_train.data)
    # news_test = dt.load_dataset('test')
    # mnb_model = multinomial_naive_bayes(idfs, news_train.target)
    #
    # predicted = prediction(mnb_model, tfidf, news_test.data)
    #
    # look_at_predictions(predicted, news_train, news_test.filenames)

    """
    SECTION #5:
        Evaluation metrics
            Notice that f1_score can be computed with different averages
            5.1 Finish metrics implementation for accuracy, precision and recall
    """

    # f1_score = metrics.f1_score(news_test.target, predicted, average='macro')
    #
    # print('Multinomial Naive Bayes model (TFIDF) F1-SCORE: '+str(f1_score))


if __name__ == '__main__':
    main()
