def BinSearch(ary,bottom,top,n):
    start = 0
    end =n
    mid = 0

    while start < end:


        mid = int (start + ( end - start) / 2)

        if (bottom> ary[mid]) and (top > ary [mid]):
            start = mid +1
            
        elif (bottom < ary[mid]) and (top < ary [mid]):
            end = mid

        else:
            return True





    return False


ary = [2,3,5,7,9,13]
            
n = 6
bottom = 4
top = 6
print (BinSearch(ary,bottom,top,n))
            
#pseudocode

BinarySearch(ary,bottom,top,n)
Start < -0 
End <-n
Mid <- 0
While start < end 
mid <- start + ( end – start) / 2
if (bottom > ary [mid]) and ( top  > ary [mid])
start <- mid + 1
else if (bottom < ary [mid]) and (top < ary [mid])
end <- mid
else return True
return False


ary < [ 2,3,5,7,9,13]

n < 6
bottom < 4
top = 6
print (BinSearch(ary,bottom,top,n)
