#text is the text we are putting through our cipher
text = ("Hello world")
#shift is the value you want to shift by in your cipher
shift = 3
#use of alphabet to shift from one character to another
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#searches variable 'alphabet' for character located at index 0 in 'text' variable
#finds the index value of this character in 'alphabet'
#assigs this index value to 'index'
#use of .lower() function so that to remove case sensitivity 
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)
