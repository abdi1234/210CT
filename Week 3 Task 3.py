def RemoveVowels(str):

    if not str:
        return ""
    if str[0] in ['a','e','i','o','u','A','E','I','O','U']:
        return RemoveVowels(str[1:])
    else :
        return str [0] + RemoveVowels(str[1:])


    


print (RemoveVowels("beautiful"))
 

#pseudocode

#NOVOWELS(str):
#      If str is empty:
#         Return str 
#If str [0] in  in ['a','e','i','o','u','A','E','I','O','U']:

#    Return RemoveVowels
#    Else:
#           Return str[0] + noVowels (str[1:])
# Str -> input string 
