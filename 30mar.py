'''
LIST COMPREHENSIONS contd
-----------------------------------------
If statement in a list comprehension
'''
#list comprehension that will produce a list of odd numbers
def oddNumbers(n):
    '''Function that generates only odd numbers between 0 and n+1

    Args: n - integer value 
    Returns : a list of odd integer values excluding 0 and including n
    '''
    return [x ** 3 for x in range(1, n+1) if x % 2 != 0]
print(oddNumbers(13))
print('---------------------------------------------------------')


def oddNumbers(n):
    '''Function that generates only odd numbers between 0 and n

    Args: n - integer value 
    Returns : a list of  odd integer values
    '''
    return [x for x in range(n) ]

print(oddNumbers(13))
print('-------------------------------------------------------------------')

'''
DICTIONARY COMPRENSION
-------------------------------
'''
#dictionary comprehension for squaring numbers
def squares_generator(num):
    return {f'{i} raised to power 2 is': i * i for i in range(1, num+1)}

print(squares_generator(9))
print('-------------------------------------------------------------------------------')

family_tree = {
    'name': 'peter dury',
    'family' : {
        'wife': 'rosemary dury',
        'children': [('tom', 'ruth'), ('william', 'grace'), ('king', 'queen')],
        'grand_children' : {
            ('tom', 'ruth'):['blue', 'purple'],
            ('william', 'grace'): ['okon', 'ekaette'],
            ('king', 'queen') : ['brown', 'dawn']
        }
    }
}

print(family_tree['family']['children'])
print(family_tree['family']['grand_children'])
print('----------------------------------------------------------------------')
print(family_tree['family']['grand_children'][('william', 'grace')])

print('---------------------------------------------------------------------------')
#python supports the unpacking of multiple values into multiple variables
children = family_tree['family']['children']
print(children)
for husband, wife in children:
    print(f'Husband is {husband} and the wife is {wife}')
grandChildren = family_tree['family']['grand_children']
print(grandChildren)
for key, value in family_tree['family'].items():
    for key1, value1 in family_tree['family']['grand_children'].items():

     print(f'the parents are {key},{key1} and the children are {value},{value1}')
'''
UNPACKING VALUES IN PY
--------------------------------------
TUPLES
 data structure in py ususally used to store values that are in pairs, i.e 
 longitudes and latitudes
'''
#python supports the unpacking of multile values into multiple variables

'''
#write a function that will skip elements of a list containing every other element from an input list 
starting with the first element .
the function uses a for loop toiterate through the elements in the input list
initialize variables
iterate through the list 
'''
def skipElements(elements):
    newList = []
    for element in elements[::2]:
      
          newList.append(element)
    return newList

print(skipElements(['a','b', 'c', 'd', 'e', 'f', 'g' ])) #should print ['a','c' 'e', 'g']
#OR

def skip_elements_using_enumerate(elements):
    new_list = []
    for index, element in enumerate(elements):
        #enumerate takes the items in an iterable and gives them each an index
        if index % 2 ==0:
           new_list.append(element)
           continue
        return new_list
print(skip_elements_using_enumerate(['a','b', 'c', 'd', 'e', 'f', 'g' ])) #should print ['a','c' 'e', 'g']
for index, element in enumerate(['a','b', 'c', 'd', 'e', 'f', 'g' ]):
    print(f'{index}-{element}')