def test():
    inum = int(input('What nuumber would you like to check? '))
    x = float(1)
    y = int(0)
    while x >= .5:
        x = x*((inum-y)/inum)
        y = y + 1
    print(x)
    return y



print(test())
