def sum(*args):
    if len(args)>0:
        s=0
        for arg in args:
            s+=arg
        return s
    else:
        return False

def product(*args):
    if len(args)>0:
        p=1
        for arg in args:
            p*=arg
        return p
    else:
        return False

def sum_quadratic(*args):
    if len(args)>0:
        s2=0
        for arg in args:
            s2+=arg**2
        return s2
    else:
        return False