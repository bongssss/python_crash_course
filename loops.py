'''
loops exercise 61
print("Input some integers to calculate their sum and average. Input 0 to exit.")
count = 0
sum = 0
number = 1

while number != 0:
  number = int(input())
  sum = sum + number
  count += 1

if count == 1:
  print("Input some numbers")
else:
  average = sum / (count - 1)
  average = float('{:.3f}'.format(average))
  print("Average of the above numbers are: ", average)
  '''
'''
loops exercise 62

prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount =  round(0.6, 2)
newprice =  [round(price * discount, 2) for price in prices]
print(newprice)


'''
'''
#loops exercise 63

print('*******Temperature converter********')
print('|------------------------------------|')
print('| Celcius\t | Farenheit |')
print('**************************************')
for celcius in range(101):
    if(celcius % 10 == 0):
        farenheit = (celcius * (9/5)) + 32
        print('\t', celcius, '\t|\t', farenheit, '\t')

'''
'''
#area in feet
unit = 'feet'
length = float(input('length in feet  '))
width = float(input('width in feet '))

area = float((width * length))
print(area, unit)
'''

'''
#area from feet to acre
unit = 'acres'
length = float(input('length in square feet  '))
width = float(input('width insquare feet '))

area = float(((width * length) / 43560 ))
print('The area of the farmers land is ',area, unit, 'of farmland')
'''


#amount of refund

numberofcontainers = int(input('Number of containers: '))
size = float(input('Size in litres: '))
if size > 1:
    refund = round(0.256 * numberofcontainers, 4)
elif size <= 1:
    refund = round(0.10 * numberofcontainers, 4)
print('For', numberofcontainers, 'number of bottles of', size, 'size, the refund amount is $',refund)