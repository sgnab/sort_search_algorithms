import random
def bubble_sort(num):
    if len(num)==0 or len(num)==1:
        return num
    for i in xrange(len(num)-1):
        for j in xrange(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num
c = random.sample(range(1,10),9)
print bubble_sort(c)