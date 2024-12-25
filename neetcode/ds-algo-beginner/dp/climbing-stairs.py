


#0 1 2 3 4 5
#8 5 3 2 1 1

def some(n):
    one, two = 1, 1

    for i in range(n-1):
        tmp = one
        one = two + one
        two = tmp
    return one 
