#!/bin/python
import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the powerSum function below.
def powerSum(X, N):
    ways=0
    max_limit=int(math.sqrt(X))
    list_nn=[n for n in range(1,max_limit+1)]
    for l in range(1,len(list_nn)+1):
        comb = combinations(list_nn, l)
        comb=[e for e in comb]

        for e in comb:
            SUM=0
            for ee in e:
                SUM+=(ee**N)
            if SUM==X:
                ways+=1
    return(ways)


print(powerSum(800,2))
