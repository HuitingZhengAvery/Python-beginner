smallest=None
largest=None
while True:
    num=input('Enter a number: ')
    if num=='done':
        break
    try:
        num=int(num)
        if smallest is None:
            smallest=num
        if largest is None:
            largest=num
        elif smallest>num:
            smallest=num
        elif largest<num:
            largest=num
            continue
    except:
        print('Invalid input')
        continue
print('Maximum is',largest)
print('Minimum is',smallest)
