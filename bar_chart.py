from random import randint

ROLLS = 100
MAX = 10
results = {} # empty dictionary
for i in range(ROLLS):
    n = randint(1,MAX)
    results[n] = results[n] + 1 if n in results else 1

for n in results:
    bar = '*' * results[n]
    print str(n) + "(" + str(results[n]) + "):\t\t" + bar