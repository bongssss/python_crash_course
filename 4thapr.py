'''
strings:
A string is a sequence of unicode characters.
- A character is simply a symbol. For example, 
the English language has 26 characters [ strings are immutable.
This means that elements of a string cannot be changed once they have been assigned.
But we can simply reassign differnet strings to the same name.
- We cannot delete or remove characters from a string. But deleting the string entirely is possible.
- Joining two or more strings into a single one is called concatenation
'''
# defining strings
single_quote = 'Hello string'
double_quote = "Hello double quote string" 
triple_quote ='''Hello triple
                        quote string'''




#triple quote strings can extend to multiple lines
myString = '''Hello, wlcome to 
                  the world of python'''
print(single_quote)
print(double_quote)
print(triple_quote)
print(myString)

#strings can be multiplied by integers 'int'
'''
write a function that repeats a word twice
and finds the length of the new rpeated word
and returns the repeated word and the length.
'''

def repeatWord(word):
    new = str(word) * 2
    length = str(len(new))
    return new + length
print(repeatWord('ubong'))


'''
acessing strings using indexing
string indexing allows you to acess individual characters of a string
the index must be an integer, using a float will give you an error 'TypeError'
'''
sentence = 'quick brown fox'
word = 'quick'
print(word[0]) #first letter
#you csn use negative unmbers as well
print(sentence[-1])
 #get the last 4 letters of the word innovation
w = 'innovation'
print(w[-4:])#
print(w[5:10])
# using string slicing
'''
silcing: getting the part of a string that contains more than one character, 
ofetn called a substring range starts from  the first char of the string to one less than the last
'''

color =  'orange'
'o' in color # check if the ketter is in the word
print(color[1:6])
print(color[2:])
print(color[0:5])



'''
write a function that returns true if the first letter of the string 
is the same as the last letter of the string, false if theyre different
'''
word = str(input('any word: '))
def firstAndLast(word):
    if  str(word) == '':
        return True
    elif str(word[0]) == str(word[-1]) :
        return True
    else:
        return False

print(firstAndLast(word))