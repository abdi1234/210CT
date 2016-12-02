text= "This is awesome"
words = text.split (' ') # splits into seperate words using the spaces
i= len (words) - 1 #starts at the end of the array
text = ""
while i >= 0: 
    text+= words[i] + "" #prints each word in reverse order
    i-=1 
print (text)    


#Big0 notation is 0(n)




#TEXT < - USER INPUT
#WORDS< - SPLIT (TEXT,” ”)
#INDEX <- LENGTH(WORDS) -1
#TEXT <- “ ”
#WHILE<- INDEX  >= 0
#      TEXT += WORDS [INDEX] + “ “
#      INDEX <- INDEX - 1

#PRINT TEXT
