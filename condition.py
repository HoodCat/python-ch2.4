# if ~ else

a = 10
if a > 5:
    print('big')
else:
    print('small')

# if ~ elif ~ else

n = -2
if n > 0:
    print('positive')
elif n < 0:
    print('negative')
else:
    print('zero')

order = 'spam'
if order == 'spam':
    price = 100
elif order == 'egg':
    price = 500
elif order == 'spagetti':
    price = 2000

print(price)

# Condition Expression(ternary operator, 삼항연산자)
# in Java, s = a > 5 ? 'big' : 'small'
print('big' if a > 5 else 'small')
