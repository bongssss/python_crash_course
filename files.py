'''FILES

files are typically accessed beginning with a call to a built-in function named OPEN 
OPEN returnsa file proxy or handler
for interactions with the underlyimg file.
The open function accepts optional second parameter that determines the access mode 
The default being 'r' for reading the file



other common modes are 'w' for writing to the file (causing any existing file with the same name to be overwritten)
there is also 'a' for appending to the end of an existing file



there are other options that allow you to work with binary files 'rb' or 'wb'

after working with a file proxy, you must close the proxy with proxy close()
doing so ensures that the content of the file is saved.
'''
#fp = open('9mar.py')
#print(fp.read()) #reads the entire file
# print(fp.readline()) #reads the first line of the file
#print(fp.readlines()) #reads the entire file without the formatting


#for x in fp:
#    print(x)

#fp.close() #closes the file handler/proxy

'''fp = open('79mar.txt', 'w') #opens a file in write mode
fp.write('this isthe first line')
fp.close()'''


fp = open('79mar.txt', 'a') # write with append mode appends to the sameline in write mode
wordgroup = ['This is the firstlone of this sentence', '\n''This is the second sentence']
for line in wordgroup:
    fp.write( line )
fp.close()




'''
modify the above to append to the next line
'''