cadeia = str(input())
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

cR = []
eR = []
uR = []
pR = []

for i, j in enumerate(cadeia):
    if cadeia[i].isalpha():
        a = int(cadeia[i-2]+cadeia[i-1])
        if (cadeia[i] == 'P'):
            try:
                p.remove(a)
            except:
                pR.append(a)
        elif (cadeia[i] == 'U'):
            try:
                u.remove(a)
            except:
                uR.append(a)
        elif (cadeia[i] == 'C'):
            try:
                c.remove(a)
            except:
                cR.append(a)
        elif (cadeia[i] == 'E'):
            try:
                e.remove(a)
            except:
                eR.append(a)
                
if (len(cR) != 0):
    print("erro")
else:
    print(len(c))

if (len(eR) != 0):
    print("erro")
else:
    print(len(e))

if (len(uR) != 0):
    print("erro")
else:
    print(len(u))

if (len(pR) != 0):
    print("erro")
else:
    print(len(p))
