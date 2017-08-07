#!/usr/bin/env python

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from classifier import GNB
import json

def main():
    gnb = GNB()
    with open('train.json', 'r') as f:
        j = json.load(f)
    print(j.keys())
    X = j['states']
    Y = j['labels']
    gnb.train(X, Y)

    skl_nb = GaussianNB()
    LE = LabelEncoder()
    skl_nb.fit(X, LE.fit_transform(Y))

    with open('test.json', 'r') as f:
        j = json.load(f)

    X = j['states']
    Y = j['labels']
    score = 0
    for coords, label in zip(X,Y):
        predicted = gnb.predict(coords)
        if predicted == label:
            score += 1
        fraction_correct = float(score) / len(X)
    print("You got {0:3.2f} percent correct".format(100 * fraction_correct))

    Y_test = LE.transform(Y)
    Y_pred = skl_nb.predict(X)
    skl_fraction_correct = sum([1 for a,b in zip(Y_test, Y_pred) if a==b]) / float(len(Y_test))
    print("Sklearn got {0:3.2f} percent correct".format(100 * skl_fraction_correct))

if __name__ == "__main__":
    main()