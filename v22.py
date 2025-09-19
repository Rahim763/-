import math
def calculate_equation():
    description = input('input value x:')
    x = float(description)
    e = math.e

    if(2+x**1/x)<=0 or (2-x)<=0:
        return 'Eror, ln() need to be positive'

    a = (e**((x**x)) * math.log(2+(x**1/x))+2**x * math.log(2-x)-(e**(2/(x**x))))
    return f'answer is:{round(a,5)}'

print(calculate_equation())
