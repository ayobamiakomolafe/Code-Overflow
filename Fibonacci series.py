print'Fibonacci Series to what array(lenght/nth term) would you like to See'
num=None
while num==None:
    try:
        num=input('Enter Number:')
        int(num)
    except:
         print('Make Sure a Number is Entered')
Fibonacci=[0,1]
if num < 2:
    print(Fibonacci)
    quit
while len(Fibonacci) != num:
    new_Fibonacci=Fibonacci[-1]+Fibonacci[-2]
    Fibonacci.append(new_Fibonacci)

    
print('The Fibonacci series to the '+ `num`+ 'th number is/are:')
print(Fibonacci)

