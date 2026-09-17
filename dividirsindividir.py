
def multiplicars(a,b):
    c = 0
    for i in range(b):
        c += a
    return c

def dividirs(a,b):

    c = 0
    if b ==0:
        return "No se puede dividir entre 0"
    while a >= b:
        a = a-b
        c += 1
    return c

def modulo(a,b):

    if b == 0:
        return "No se puede dividir entre 0"
    div = dividirs(a,b)
    resto = a - multiplicars(div,b)
    return resto


a = 311
b = 15

c = dividirs(a,b)
d = multiplicars(a,b)
e = modulo(a,b)
print(c)
print(d)
print(e)