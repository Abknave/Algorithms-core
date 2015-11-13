from QuickSort import QS


def PairSum(arr,Entry):
     arr= QS(arr) #using quick sort
     left=0
     right=len(arr)-1
     while left<right:
         if(arr[left]+arr[right]==Entry):
             print str(arr[left])+" "+"and"+" "+str(arr[right])
             return True
         elif(arr[left]+arr[right]<Entry):
              left+=1
         else:
             right-=1
     print "not found"
     return False

#TEST CASES    
l=[6,5,4,2,1]

print PairSum(l,10)
print
print PairSum(l,11)
print
print PairSum(l,40)
