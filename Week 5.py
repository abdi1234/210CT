Given a sequence of n integer numbers,
extract the sub-sequence of maximum length which is in
ascending order.

myList = [1,2,1,10,4,5,1,6,78,88,99]
myList2 = myList.copy() #copy of the first list

FinalList = []

for element in myList:
    TempList = []
    for element in myList2:
        
        if len(TempList) == 0: #if the temp list is vacant append first item
            
            TempList.append(element)
        else:
            if element > TempList[-1]:
                TempList.append(element)
            else:
                myList2 = myList2[1:] #myList2 equals myList2 minus 1st element
                break
            if (len(TempList) > (len(FinalList))): #restore final list if temp list is larger
                FinalList = TempList
    
    
   
        
print(FinalList)
