## method 1
import random,time
def insert_sort(num):
    key=1
    while key<len(num):
        ind = 0
        for i in xrange(key+1):
            if num[key-ind]<num[key-i]:
                num[key-ind],num[key-i]=num[key-i],num[key-ind]
                ind += 1
            # print key - i, key-ind, num
        key+=1
    return num

# Method 2, using shifting instead of swapping
def ins_sort2(num):
    if len(num)>1:
        for i in xrange(1,len(num)):
            curr = num[i]
            for j in xrange(i-1,-1,-1):
                if num[j]>curr:
                    num[i]=num[j]
                    i-=1
                else:
                    num[i]=curr
            num[i]=curr




    return num



# b=alist.alist
t = time.time()
b = random.sample(range(1,10001),10000)
insert_sort(b)
ins_sort2(b)
print time.time()-t