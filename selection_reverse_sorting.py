####BIG O is O(n^2)
import random
def select_sort(num):
    if len(num)<=1:
        return num
    for i in xrange(len(num)):
        # print i
        for j in xrange(i,len(num)):# here if you use just xrange(len(num)), the list will be ordered in reverse
            print j
            if num[i]<num[j]:
                num[j],num[i]=num[i],num[j]
    return num

b = random.sample(range(1,10),9)

print select_sort(b)