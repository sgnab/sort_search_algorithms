import time,random
import threading
import multiprocessing
#####merge sort

def partion(num):
    if len(num)<2:
        return num
    left = num[:len(num) / 2]
    right = num[len(num) / 2:]
    # time.sleep(.2)
    left = partion(left)

    right = partion(right)
    return merging(left, right)

def merging(left,right):
    res=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res+=left[i:]
    res+=right[j:]
    return res


