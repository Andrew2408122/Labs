import math
a = 0.1
b = 0.5
h = 0.05
pes = 0.0001
x = a
while x <= b:
    o = x 
    y = math.atan(o)
    i = 0
    sum = 0
    term = 1
    while abs(term) >= pes:
        term = ((-1)**i) * ((x**(2*i + 1)) / (2*i + 1))
        sum += term
        i += 1
    print('x =',x, ';', 'Сумма =',sum, ';', 'y =',y)
    x += h
