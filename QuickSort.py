arr=[5,2,6,1,3,4]

def QuickSort(arr,start,end):
        def PARTITION(arr,start,end):
                    pivot=arr[end]
                    pIndex=start
                    for i in range(start,end):
                        if arr[i]<=pivot:
                          k=arr[i]
                          arr[i]=arr[pIndex]
                          arr[pIndex]=k
                          pIndex=pIndex+1
                    y=arr[pIndex]
                    arr[pIndex]=arr[end]
                    arr[end]=y
                    return pIndex


        if(start<=end):
                pIndex=PARTITION(arr,start,end)
                QuickSort(arr,start,pIndex-1)
                QuickSort(arr,pIndex+1,end)

        return arr        
                
        
               
print QuickSort(arr,0,len(arr)-1)
                    
                            
        
   
    
