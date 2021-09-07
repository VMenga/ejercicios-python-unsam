#propaga.py
#Por Valentin Mengascini

lista = []
def propagar(lis):
    for count in range(2):
        for i,f in enumerate(lis):
            if i - 1 >= 0 and f==0 and lis[i-1]==1:
                lis[i] = 1
        lis = lis[::-1]
    return lis
