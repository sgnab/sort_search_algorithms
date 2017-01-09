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