def multiply(start, *args):
    mult = start
    for i in args:
        mult = mult*i
        print(mult)
    return mult

result = multiply(1,2,3,4,5)
print(result)
