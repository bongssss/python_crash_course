# QUESTION 1
n = int(input('Any number: '))
def nextprime(n):
    if n == 2:
        prime = n + 1
        return prime 
      
    if n == 3:
        prime = n + 2
        return prime
    if n == 1 or n % 2 == 0:
        prime = n + 1
        return prime
    p = 3
    while p * p <= n:
        if n % p == 0:
            prime = n + 2
        p += 2
        return prime
    

nextPrime = nextprime(n)
print(f'The next prime number agter {n} is {nextPrime}')



# QUESTION2

# stirng = input('Any hexaecimal number between 1 and 15: ')
# def hex2int(string):
#     value = int(string, 16)
#     return value

# int_value =hex2int(stirng)
# print(int_value)


# integer = int(input('Any number in base 10 from 1 to 15: '))
# def int2hex(integer):
#     hexadecimal = hex(integer)
#     return hexadecimal

# hex_value =int2hex(integer)
# print(hex_value)


#QUESTION 2 AGAIN

