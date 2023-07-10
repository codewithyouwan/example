import math
def calculator(x,y,string):
    match string:
        case '*':
            return x*y
        case '/':
            return x/y
        case '+':
            return x+y
        case '-':
            return x-y
        case _:
            return "Not valid input"
    
def mainfunction():
    a=[]
    while (True):
       b=input()
       if(len(b)==0):
           break
       a.append(b) 
    print('[ ')
    for i in range(0,len(a)):
        print(a[i],' ')
    print(']','Thanks')
        
mainfunction()