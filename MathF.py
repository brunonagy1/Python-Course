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