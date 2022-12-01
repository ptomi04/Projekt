
karkes=""
jf=open('mksz.txt','r', encoding='utf-8')
karkes = jf.readline()
jf.close()

def karsz(karakter):
    I=0
    h=0
    while(karkes[I] != karakter):
        if I < (len(karkes))-1:
            I = I + 1
        else:
            break
            I=55

    return I


def koder(szoveg,paswd):
    er=""
    i=0
    j = 0
    keszkod = ""

    for i in range(len(szoveg)):

        if (len(paswd) <= j):
            j = 0

        er = karsz(szoveg[i]) + karsz(paswd[j])

        if (er >= len(karkes)):
            er = er - len(karkes)


        keszkod = keszkod + karkes[er]
        i = i + 1
        j = j + 1
    return keszkod

def dekoder(szoveg,paswd):
    j = 0
    er=""
    keszkod = ""

    for i in range(len(szoveg)):

        if (len(paswd) <= j):
            j = 0

        er = karsz(szoveg[i]) - karsz(paswd[j])

        if (0 > er):
            er = er + len(karkes)
        keszkod = keszkod + karkes[er]
        i = i + 1
        j = j + 1
    return keszkod
