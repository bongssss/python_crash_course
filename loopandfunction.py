#INT2HEX
number = int(input('any nmber in base10: '))
def int2hex(number):
    hexnum = ''
    if number == 0:
        print('0')
    while number > 0:
        remainder = number % 16
        if remainder == 10:
            remainder = 'A'
        elif remainder == 11:
            remainder = 'B'
        elif remainder == 12:
            remainder = 'C'
        elif remainder == 13:
            remainder = 'D'
        elif remainder == 14:
            remainder = 'E'
        elif remainder == 15:
            remainder  = 'F'
        
        hexnum = str(remainder) + hexnum #WRRITING THE REMAINDERS BACKWARDS
        number = number // 16 # FLOOR DIVISION ROUNDS THE WHOLENUMBER TO THE NEAREST INTEGER


    print(hexnum)


answer = int2hex(number) 



#HEX2INT
hex2intdict ={'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, 
              '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
hexno = input('Any hexadecimal number: ').upper()
baseTen = 0
length = len(hexno) - 1
for value in hexno:
    baseTen += hex2intdict[value] * 16 ** length
    length -= 1

print(baseTen)

