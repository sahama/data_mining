import itertools
def findsubsets(S):
    result = []
    for i in range(len(S)):
        result += list(set(itertools.combinations(S, i+1)))

    return [set(i) for i in result]

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'

all_transaction = [
    {a,b,d,e},
    {b,c,d},
    {a,b,d,e},
    {a,c,d,e},
    {b,c,d,e},
    {b,d,e},
    {c,d},
    {a,b,c},
    {a,d,e},
    {b,d}
]

S = {a,b,c,d,e}

for subset in findsubsets(S):
    c = 0
    for transaction in all_transaction:
        if subset.issubset(transaction):
            c += 1
    print(sorted(list(subset)), "min sup = {}".format(c))



