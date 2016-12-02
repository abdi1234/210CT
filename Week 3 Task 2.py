def checkprime (x,div):
    if div == 1: #this is the base case
        return True
    if x % div == 0: # checking if x is divisble by div 
        return False
    else:
        return checkprime(x,div -1) 



x=int(input("Enter number:"))
div = x - 1


print (checkprime(x,div))


#pseudocode
 
 
# Function is checkprime(x,div):
#    if div <- 1
    
#        return True
    
#    if mod x div == 0

#        return False

#    else

#    return check prime(x,div)
