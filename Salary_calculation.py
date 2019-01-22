hrs=input('enter hours:')
rate=input('enter rate:')
def computepay(h,r):
    h=float(h)
    r=float(r)
    if 0<=h<=40:
        return h*r
    elif h>40:
        return (h-40)*r*1.5+40*r
    else:
        return 'invalid input, please try again'
print(computepay(hrs,rate))
