from numpy import array

def stepfun(t,t0):
    y = []
    for i in t:
        if i>=t0:
            y.append(1)
        else:
            y.append(0)
    return array(y)