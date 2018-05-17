import nltk # needed for Naive-Bayes
import numpy as np
from sklearn.model_selection import KFold
import math

def coba1():
    # data is an array with our already pre-processed dataset examples
    kf = KFold(n_splits=3)
    sum = 0
    data = [2,3,5,1,7,1,6,3,2,5,8,3]
    for train, test in kf.split(data):
        train_data = np.array(data)[train]
        test_data = np.array(data)[test]
        print(train_data)
        print("test data :", test_data)
        # classifier = nltk.NaiveBayesClassifier.train(train_data)
        # sum += nltk.classify.accuracy(classifier, test_data)
    # average = sum/3

def coba2():
    training = [[2.11,2,3,4],[5,6,7,8],[9,10,11,12],[9,3,6,2],[3,6,3,8],[3,8,8,9],[12,24,6,12],[22,25,63,11]]
    num_folds = 3
    subset_size = int(len(training) / num_folds)
    for i in range(num_folds):
        testing_this_round = training[i * subset_size:][:subset_size]
        training_this_round = training[:i * subset_size] + training[(i + 1) * subset_size:]
        print('\n')
        print('============== k',i+1,' ==============')
        print('training : ',training_this_round)
        print('testing : ', testing_this_round)
        # train using training_this_round
        # evaluate against testing_this_round
        # save accuracy

def coba3():
    training = [5, 6, 4, 8]
    pindah = np.array(training)
    datanya = [5, 4, 7, 8]

    for i in [i for i,x in enumerate(training) if x in datanya]:
        print(i)

    k = 2
    idx = np.argpartition(pindah, k)
    hasil = pindah[idx[:k]]
    print(hasil)

coba3()