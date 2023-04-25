'''
Builtin functions used with strings
Various built in functions that work with sequence work with strings as well.
# Some common ones are: enumerate(), len(), upper(), lower(), split(), join)
- enumerate() returns an enumarated object 
i.e. a pair or tuple of index and value of all the items in the string.
Very useful for iteration.
'''

#to know what the index of a letter is in a string
#the index() returns the index of the substringpassed into it
# the index() returns just the first position that matches
pets = 'Cats & Dogs'
pets.index('D')
pets.index('Cats')
pets.index('s')


#Deleting an entire string
to_be_deleted =  'this string will soon be deleted'
del to_be_deleted

# you can iterate through a string using for the loop
# the string is a squence
for letter in 'Hello world':
    print(letter)


print('---------------------------------------------------------------------------------')
count = 0
for letter in 'Hello world':
       if letter == 'l':
           count +=1

print(str(count) + " 'l' letters found")


#example using index method
'''
using the index method, find out the position of 'x' in 
"supercalifragilisticexpialidocious"
'''
print('---------------------------------------------------------------------------------')
word = "supercalifragilisticexpialidocious"
print(word.index('x'))

print('---------------------------------------------------------------------------------')
#to know if a substring is contained in a string - string membership test
# a membership test returns true or false
pet = 'Cats & Dogs'
print('Cats' in pet)
print('Dragons' in pet)



'''
Realworld application:
write a function that finds an email and 
replaces the domain with a new company's domain

example
johndoe@gmail.com - johndoe@starthub.com

take an email, take the old domain and take the newdomain as parameters
'''

oldDomain = str(input('@gmail.com: '))
string = str(input('name: '))
email= string + oldDomain
newDomain = '@starthub.com'
def changeDomain(oldDomain, email, newDomain):
     if email == string + oldDomain:
          new = email = string + newDomain
          return new
        

print('was '+ email + '  but is now  ' + changeDomain(oldDomain, email, newDomain))

# OR using indexing
print('------------------------------------------------------------------------------------------------')
#mail = str(input('enter an email: '))
#olddomain = 'uestc.edu.cn'
#newdomain =  'starthub.com'
def replaceDomain(mail, olddomain, newdomain):
     
     if '@' + olddomain in mail:
          index = mail.index('@' + olddomain)
          newMail = mail[:index] + '@' + newdomain
          return newMail
     return mail
print(replaceDomain( 'ubong@uestc.edu.cn', 'uestc.edu.cn', 'starthub.com'))



print('----------------------------------------------------------------------------------------------------')

def get_emails(file_path):
     email_list = [] 
     with open(file_path, "r") as df:
          for line in df.readlines():
               email_list.append(line)
     return email_list

def replac_domain(olddomain, newdomain, emails):
     new_email = []
     for email in emails:
          if "@" + olddomain in email:
               index = email.index("@" + olddomain)
               new_email.append(email[:index] + "@" + newdomain)
          else:
               new_email.append (email)
     return new_email


emails = get_emails("emails.txt")
print (replac_domain("mail.com","starthub.com", emails))
