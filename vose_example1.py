
from vose import Vose

### Example 1: Using a List of Weights


# Assume there are three events with weights 10, 30, and 60
weights = [10, 30, 60]

# Create the sampler
sampler = Vose(weights)

# Draw a single sample
single_sample = sampler.sample()
print(f"Single sample: {single_sample}")

# Draw 10 samples
samples = sampler.sample(size=10)
print(f"10 samples: {samples}")

# Validate the sampling distribution (by drawing a large number of samples)
from collections import Counter
many_samples = sampler.sample(size=10000)
counts = Counter(many_samples)
print(f"Statistics from 10,000 samples: {counts}") 
# Expected output: {0: ~1000, 1: ~3000, 2: ~6000}