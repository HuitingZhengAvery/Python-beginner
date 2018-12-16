score=input('Enter Score:')
x=float(score)
if x<0.0:
    print('Error, please enter a number between 0.0 and 1.0')
if x>1.0:
    print('Error, please enter a number between 0.0 and 1.0')
elif 0.0<=x<0.6:
    print('F')
elif 0.6<=x<0.7:
    print('D')
elif 0.7<=x<0.8:
    print('C')
elif 0.8<=x<0.9:
    print('B')
elif 0.9<=x<=1.0:
    print('A')
