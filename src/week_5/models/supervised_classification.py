from sklearn.naive_bayes import MultinomialNB


def multinomial_naive_bayes(c_index, dataset_target):
    mnb_model = MultinomialNB().fit(c_index, dataset_target)

    return mnb_model


def prediction(model, vect, dataset_test):
    tranf_dtest = vect.transform(dataset_test)
    predicted = model.predict(tranf_dtest)

    return predicted


def look_at_predictions(predicted, dataset_train, dataset_test):
    for sample, class_pos in zip(dataset_test, predicted):
        print('%r => %s' % (sample, dataset_train.target_names[class_pos]))


def svm(c_index, dataset_target):
    # fit the model and get the separating hyperplane
    # penalty parameter C of the error term with the default value of 1.0
    model = svm.SVC(kernel='linear', C=1.0)
    model.fit(c_index, dataset_target)

    return model

