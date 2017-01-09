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



# quick sort

def q_sort(num,low,hi):
    if low<hi:
        # time.sleep(.2)
        piv = partition(num,low,hi)
        q_sort(num,low,piv-1)
        q_sort(num,piv+1,hi)
        return num


def partition(num,low,hi):
    wall,curr=low,low
    piv=hi
    # for curr in xrange(low,hi):

    while curr<=hi:
        if num[curr]<num[piv]:
            num[curr],num[wall]=num[wall],num[curr]
            curr+=1

            # print curr
            wall+=1
        else:
            curr+=1

    num[piv],num[wall]=num[wall],num[piv]

    return wall



t=time.time()



####multi_processing
if __name__=="__main__":
    b = random.sample(range(1, 1000001), 1000000)

    t1 = multiprocessing.Process(target=partion, args=(b,))
    t2 = multiprocessing.Process(target=q_sort, args=(b,0,len(b)-1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


#### multi_threading does not work very well in this case
# if __name__=="__main__":
#     b = random.sample(range(1, 1000001), 1000000)
#
#     t1 = threading.Thread(target=partion, args=(b,))
#     t2 = threading.Thread(target=q_sort, args=(b, 0, len(b) - 1,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


# partion(b)
# q_sort(b,0,len(b)-1)
print time.time()-t


