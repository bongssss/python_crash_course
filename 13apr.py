'''
write a program that reads froma file of emailadresses and 
replaces all the domains of the email addresses with a new one @king.com
'''
def getEmails(filePath):
    listOfEmails = ''

    with open(filePath, 'r') as mails:
        for line in mails.readlines():
           
            listOfEmails += line
   # print(listOfEmails)
    return listOfEmails
emails = getEmails('emails.txt')

def newDomain(emails, oldDomain, newDomain):
    newMail= ''
    

    for email in emails:
        if '@' + oldDomain in emails:
            index = email.index('@' + oldDomain)
            n = email[:index] + '@' + newDomain
            newMail += n
    return newMail



print(newDomain(emails, 'mail.com', 'king.com'))