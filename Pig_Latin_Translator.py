print 'Welcome to the Pig Latin Translator!'
#Variable declaration
pyg = 'ay'
#Initiates parameter input
original = raw_input('Enter a word:')
#If statement to evaluate parameter input
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg 
    print'Pig Latin Transalation:'+ new_word 
else:
    print 'empty'