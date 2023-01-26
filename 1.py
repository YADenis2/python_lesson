def a(U0, T, U):
    return(U0-U)/T
def s(a):
    global temp
    def dec():
        A = a
        return U0*T-(A*T*T/2)
    return dec()
def inp():
    global U0, T, U
    try:
        temp = input(">> U0, T, U  ").split()
        U0 = int(temp[0])
        T = int(temp[1])
        U = int(temp[2])
    except TypeError:
        print("Введите числа")
        inp()
    if T == 0:
        print("T!=0")
        inp()
inp()
print(s(a(U0, U, T)))
        
