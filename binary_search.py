import random
import alist
def guess(n):
    if n<105:
        return +1
    elif n>105:
        return -1
    else:
        return 2
def bsearch(num):
    min=0
    max=len(num)-1

    while min<max:
        ind = (min + max) // 2
        guess1 = num[ind]
        if guess(guess1)==2:
            return guess1, 'You won'
        elif guess(guess1)==-1:
            max=max-1
            min=min
        else:
            min=min+1
            max=max

b=range(1000)
print bsearch(b)

