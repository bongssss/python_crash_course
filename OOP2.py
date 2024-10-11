'''
implement a banking system in a python object
 custimer; withdraw, deposit and update details

'''
from abc import ABC
class Banking_system(ABC):
    def __init__(self, name, balance, currency, accountnumber, withdrawamount, depositamount):
        self.name = name
        self._account = accountnumber
        self._balance = balance
        self.currency = currency
        self.withdrawal = withdrawamount
        self.deposit = depositamount

    def welcome(self):
        print(f'welcome {self.name}, your account number is {self._account}')

    def checkBalance(self):
       print(f'{self.name}, your current account balance is {self.currency}{self._balance}')
    
    def withdraw(self,  ):
       #int(input('withdraw amount: '))
       if self._balance < self.withdrawal:
           print(f'insufficient funds, you cannot withdraw {self.currency}{self.withdrawal} ')
       else:
        self._balance = self._balance - self.withdrawal
        print( f'your balance is {self._balance}')
        

    def setDeposit(self, ):
        #int(input('deposit: ')) 
        self._balance = self._balance + self.deposit
        print ( f'new balance after deposit is {self.currency}{self._balance}')
    
        

    def updateDetails(self):
       print( f'your bank infotmation for {self._account } is up to date at {self.currency}{self._balance}')



customer1 = Banking_system('Ubong', 50000, 'N', '00012A', 62000, 5000)
customer1.welcome()
customer1.checkBalance()
customer1.withdraw()
customer1.setDeposit()
customer1.updateDetails()
    
        

   