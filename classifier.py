from math import pi, sqrt, exp, log

class GNB(object):
    def __init__(self):
        self.possible_labels = ['left', 'keep', 'right']
        self.priors = {label: 0.0 for label in self.possible_labels}
        self.mean = {label: dict() for label in self.possible_labels}
        self.variance = {label: dict() for label in self.possible_labels}

    def gaussian_proba(self, obs, mean, variance):
        # Input the arguments into a probability density function
        proba = 1.0 / (sqrt(2.0 * pi * variance)) * exp((-(obs - mean) ** 2.0) / (2.0 * variance))
        return proba

    def compute_priors(self, labels):
        examples = float(len(labels))
        for label in labels:
            self.priors[label] += 1.0 / examples
        print("Priors:", self.priors)

    def compute_mean(self, data, labels):
        if sum(self.priors.values()) < 0.99:
            self.compute_priors(labels)
        vars = len(data[0])
        examples = float(len(labels))
        counts = {label: self.priors[label] * examples for label in self.possible_labels}
        for row, label in zip(data, labels):
            for var in range(vars):
                if var in self.mean[label]:
                    self.mean[label][var] += row[var] / counts[label]
                else:
                    self.mean[label][var] = row[var] / counts[label]
        print("Means:", self.mean)

    def compute_variance(self, data, labels):
        if sum(self.priors.values()) < 0.99:
            self.compute_priors(labels)
        vars = len(data[0])
        examples = float(len(labels))
        counts = {label: self.priors[label] * examples for label in self.possible_labels}
        for row, label in zip(data, labels):
            for var in range(vars):
                if var in self.variance[label]:
                    self.variance[label][var] += (row[var] - self.mean[label][var])**2 / counts[label]
                else:
                    self.variance[label][var] = (row[var] - self.mean[label][var])**2 / counts[label]
        print("Variances:", self.variance)

    def train(self, data, labels):
        """
        Trains the classifier with N data points and labels.

        INPUTS
        data - array of N observations
          - Each observation is a tuple with 4 values: s, d,
            s_dot and d_dot.
          - Example : [
                [3.5, 0.1, 5.9, -0.02],
                [8.0, -0.3, 3.0, 2.2],
                ...
            ]

        labels - array of N labels
          - Each label is one of "left", "keep", or "right".
        """
        self.compute_priors(labels)
        self.compute_mean(data, labels)
        self.compute_variance(data, labels)

    def predict(self, observation):
        """
        Once trained, this method is called and expected to return
        a predicted behavior for the given observation.

        INPUTS

        observation - a 4 tuple with s, d, s_dot, d_dot.
          - Example: [3.5, 0.1, 8.5, -0.2]

        OUTPUT

        A label representing the best guess of the classifier. Can
        be one of "left", "keep" or "right".
        """

        naive_bayes_score = list()

        for position, label in enumerate(self.possible_labels):
            naive_bayes_score.append(log(self.priors[label]))
            for feature, obs in enumerate(observation):
                naive_bayes_score[position] += log(self.gaussian_proba(obs, self.mean[label][feature], self.variance[label][feature]))

        return self.possible_labels[naive_bayes_score.index(max(naive_bayes_score))]