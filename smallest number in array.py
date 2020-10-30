print'Continue Entering number for the array, when all numbers in array are entered type-in done '
array=list()

while True:
    num=raw_input('Enter Number:')
    try:
        if num == 'done':
            break
        else:
            array.append(int(num))
            
    except:
        print('\nPlease make Sure a Number is Entered, When you are done entering desired number in array\ntype-in done \n')
        continue

smallest=(min(array))

print('\n')
print('The smallest number in the array is '+ `smallest`)



    
    
