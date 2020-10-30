Ok='No'
while Ok=='No':
    num=raw_input('Enter Number: ')
    power=raw_input('To What Power:')
    try:
        num=int(num)
        power=int(power)
        Ok='yes'
    except:
        print('Make sure a Number has been Entered ')

Answer=num
if power == 0:
    Answer=1
else:
    for i in range(power-1):
        Answer=Answer*num
 
print `num`+ '^' + `power` + '=' + `Answer`        

