from vose import Vose

# Define each outcome and its corresponding weight
outcome_weights = {
    "apple": 0.2,
    "banana": 0.5,
    "cherry": 0.3
}

# Create the sampler
fruit_sampler = VoseAlias(outcome_weights)

# Draw a random fruit
random_fruit = fruit_sampler.sample()
print(f"\nA randomly drawn fruit is: {random_fruit}")

# Draw 5 random fruits
random_fruits = fruit_sampler.sample(size=5)
print(f"5 randomly drawn fruits: {random_fruits}")

# Validate the sampling distribution
from collections import Counter
many_fruits = fruit_sampler.sample(size=10000)
fruit_counts = Counter(many_fruits)
print(f"Statistics from 10,000 samples: {fruit_counts}")
# Expected output: {'banana': ~5000, 'cherry': ~3000, 'apple': ~2000}