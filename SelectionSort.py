def SelectionSort(l):
    array=[0 for i in range(len(l))]
    maximum=(2**32)-1
    aux=0
    for i in range(len(l)):
           pivot=l[0]
           for j in range(1,len(l)):
               if (pivot>=l[j]):
                      pivot=l[j]
                      aux=j
           
           array[i]=pivot
           l[aux]=maximum
           print l
    return array

l=[5,4,3,2,1,5,4,3,2,1]
print SelectionSort(l)
           
               
               
                               
               
               
