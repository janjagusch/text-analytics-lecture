def look_at_features(tfidf, response):
    """
    Args:
        tfidf: weighting scheme trained with a specific dataset
        response: the weights given to each term by tfidf
    Returns:
        A list of terms and the respective tfidf weight (zero values will be ignored)
    """

    feature_names = tfidf.get_feature_names()

    for col in response.nonzero()[1]:
        print feature_names[col], ' - ', response[0, col]