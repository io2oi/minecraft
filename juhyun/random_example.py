import random

a = 90
b = 100
X = 1000000000000000000
for ii in range(100):
    print(random.randint(a, b))

print(f"{0.025 * X/100/60/60/24/365/100000000} 억년")