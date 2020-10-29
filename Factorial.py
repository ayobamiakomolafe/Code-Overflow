print('What Number Would you like to Find its Factorial:')


ok=None
while ok==None:
    num=raw_input ('Enter Number:')
    try:
        num=int(num)
        ok='Good'
    except:
        print('Make Sure a Number is Entered')
    
    
difference=list()
difference.append(num)
number=num
d=None
while d !=1:
    subtraction=number-1
    d=subtraction
    number=subtraction
    difference.append(subtraction)

Factorial=1
for i in difference:
    Factorial=Factorial*i

print('The Factorial of ' + `num` + ' is '+ `Factorial`)
    
    
    
    
