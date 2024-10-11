processId = [19802, 5612, 6712]
service = 1 + 1

def retry(service):
    if service < 50:
        service += 5
        print(f'service was performed {service} times')
    
    else:
        print('sucessfull')
print(retry(service))

'''
Write a program that retries an operation a certain number of times.
The program should print how many attemps succeded and how many failed
'''




process_id = [19802, 5612, 6712]
def stop_service(pid):
    if pid in process_id:
      return True
    return False
    

#answer
def retry(opreation, attempts):
   for n in range(attempts):
      if opreation:
        print (f"Successfull attempt {n}")
        break 
      else:
        print(f'Attempt failed {n}')