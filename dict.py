#assignment: create an add_prices function that returns the total price of all of the grocaries in the dctionary.


#SOLUTION




#dictionary
groceries = { 'apple ': 2,
             'orange': 3,
             'grape': 5,
             'groundnut': 4}


#function add_prices returns the total price of the grocaries in a shopping cart; cart = argument
def add_prices(cart):
  
  
   #initialise the variable that will be used to store the sum of prices.
       totalprice = 0
       
       #loop through the items in the dictionary
       for  item, price in cart.items():
         
         #add the prices od all dictionary items to the total price 
            totalprice += price
        

         
         
         #return the total prices by using the print statement and calling the add_prices function
       print(add_prices(cart)) 