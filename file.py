ot = input('Дата рождения от (через пробел)').split()
Do = input('Дата рождения до (через пробел)').split()
with open('Perepis.txt', 'r') as file:
    try:
        while True:
            a = file.readline().split()
            if int(a[3].split('.')[2] ) < 1978:
                print(a[0], a[1], a[2], "родился до 1978")
            if int(a[3].split('.')[2]) > int(ot[2]) and int(a[3].split('.')[2]) < int(Do[2]):
                if int(a[3].split('.')[1]) > int(ot[1]) and int(a[3].split('.')[1]) < int(Do[1]):
                    if int(a[3].split('.')[0]) > int(ot[0]) and int(a[3].split('.')[0]) < int(Do[0]):
                        print("Также ", a[0], a[1], a[2], ' в указанном вами диапазоне')
    except:
        print('end')
    file.close()
