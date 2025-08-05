#!/usr/bin python
"""
Vose alias method for random sampling in python 

https://github.com/node/vose

"""

__author__ = 'Chris Yang'
__version__ = '0.1'

import random

class Vose:
	"""
    An implementation of Vose's Alias Method, used for efficient sampling from a
    discrete probability distribution. This method requires O(n) preprocessing time,
    after which each sample can be drawn in O(1) time.

    Attributes:
        prob (list[float]): Stores the probability for each index.
        alias (list[int]): Stores the alias for each index.
        n (int): The number of events in the distribution.
    """

    def __init__(self, weights):
        """
        Initializes the VoseAlias sampler with the given weights.

        Args:
            weights (dict[any, float] or list[float]): 
                A dictionary containing outcomes and their corresponding weights,
                or a list of weights. Weights must be non-negative.
        
        Raises:
            ValueError: If the list of weights is empty or contains negative values.
            TypeError: If weights is not a list or a dictionary.
        """
        if isinstance(weights, dict):
            self.outcomes = list(weights.keys())
            self.weights = list(weights.values())
        elif isinstance(weights, list):
            self.outcomes = list(range(len(weights)))
            self.weights = weights
        else:
            raise TypeError("Weights must be a list or a dictionary.")

        if not self.weights:
            raise ValueError("The weights list cannot be empty.")

        self.n = len(self.weights)
        total_weight = sum(self.weights)
        
        if total_weight <= 0:
            raise ValueError("The sum of all weights must be positive.")

        # Normalize probabilities
        self.prob = [w * self.n / total_weight for w in self.weights]

        # Initialize small and large lists
        small = []
        large = []

        for i, p in enumerate(self.prob):
            if p < 1.0:
                small.append(i)
            else:
                large.append(i)

        self.alias = [0] * self.n

        # Populate the alias and prob tables
        while small and large:
            s = small.pop()
            l = large.pop()

            self.alias[s] = l
            self.prob[l] = self.prob[l] + self.prob[s] - 1.0

            if self.prob[l] < 1.0:
                small.append(l)
            else:
                large.append(l)

    def sample(self, size=None):
        """
        Draws one or more samples from the distribution.

        Args:
            size (int, optional): The number of samples to draw. If None,
                                  a single sample is returned.

        Returns:
            any or list[any]: A single sample or a list of samples.
        """
        if self.n == 0:
            return None if size is None else []

        if size is None:
            return self._get_single_sample()

        return [self._get_single_sample() for _ in range(size)]

    def _get_single_sample(self):
        """Draw a single sample."""
        i = random.randrange(self.n)
        if random.random() < self.prob[i]:
            return self.outcomes[i]
        else:
            return self.outcomes[self.alias[i]]



if __name__ == '__main__':
	pass

# END
