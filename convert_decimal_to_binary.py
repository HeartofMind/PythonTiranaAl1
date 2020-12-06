def Converter(nr):
    x = nr
    binary = []
    while nr > 0:
        r = int(float(nr % 2))
        binary.append(r)
        nr = (nr - r) / 2
    binary.append(0)
    string = ""
    for j in binary[::-1]:
        string = string + str(j)
    print('The binary nr for %d is %s' % (x, string))


Converter(5)
