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



print 'The Number(s) you Entered are: '
print(array)
print 'And The reverse of the array you Entered is :'

# finding the reverse of the array
rev=-1
reverse=list()
for i in range(len(array)):
    reverse.append(array[rev])
    rev=rev-1
    continue
print reverse
    
    
    
    
    
