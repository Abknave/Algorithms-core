from QuickSort import QS
inp =[2,2,2,3,3,3,3,5,6]
def MajorityElement(arr):
    arr=QS(arr)
    print arr
    count=1
    maxcount=1
    i=0
    const=1
    number=1
    while(i+1<=len(arr)-1):
        
        if(arr[i]==arr[i+1]):
               count+=1
               if(i+1==len(arr)-1):
                 if(maxcount<count):
                       maxcount=count
                 elif(maxcount==count):
                        const=const+1
        else:
            number+=1
              
            if(maxcount==count):
                     const=const+1
                     maxcount=count

            if(maxcount<count):
                maxcount=count
           
            count=1
        i+=1


      
    if(const==number):
               return None
    if(i==len(arr)-1):
            count=maxcount
            return count
            

        
    
print MajorityElement(inp)
        
             

