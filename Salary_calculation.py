hrs=input('Enter Hours:')
rate=input('Enter Rate:')
x=float(hrs)
y=float(rate)
if x>40:
    pay=40*y+(x-40)*y*1.5
else:
    pay=x*y
print(pay)
