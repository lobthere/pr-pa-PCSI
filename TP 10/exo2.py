def euclide(a: int, b: int):
    assert a >= 0
    assert b > 0
    x, y = a , b
    while y!=0:
        #x, y = y, x%y
        r = x%y
        x,y = y,r
    return x

a= 2*(5**2)*7*11
b = (3**3)*5*11*13

print(euclide(a,b))