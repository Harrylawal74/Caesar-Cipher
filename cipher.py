text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#searches variable 'alphabet' for character located at index 0 in 'text' variable
#finds the index value of this character in 'alphabet'
#assigs this index value to 'index'
#use of .lower() function so that to remove case sensitivity 
index = alphabet.find(text[0].lower())
print(index)