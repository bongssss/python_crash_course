def mod():
    print(f'The making of my very own python module, {__name__}, sit back, relax and enjoy :)')
    

__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__testubong__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")
