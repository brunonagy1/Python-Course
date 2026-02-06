def sum_arg(*args):
    s=0
    for arg in args:
        s+=arg
    return s

def product_arg(*args):
    if len(args)>0:
        p=1
        for arg in args:
            p*=arg
        return p
    else:
        return False
    
def decorator(func):
    def wrapper(x:int)->int:
        return func(x)*2
    return wrapper

@decorator
def number(y:int)->int:
    return 2*y

@decorator
def sara(y:float)->float:
    return 3*y

print(number(5))
print(sara(10))
print(1)
