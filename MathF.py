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
def dec1(func):
    def wrapper(s:str)->str:
        return func(s).upper()
    return wrapper

@dec1
def f1(s:str)->str:
    return s+"n"

print(f1("Bruno"))

