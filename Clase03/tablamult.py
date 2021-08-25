#tablamult.py
#Por Valentin Mengascini

print('       0   1   2   3   4   5   6   7   8   9')
print('---------------------------------------------')
for mult in range(10):
    list = []
    for counter in range(10):
        num = 0
        num += counter*mult
        list.append(num)
    print(f'{mult:^4d}{list[0]:>4d}{list[1]:>4d}{list[2]:>4d}{list[3]:>4d}{list[4]:>4d}{list[5]:>4d}{list[6]:>4d}{list[7]:>4d}{list[8]:>4d}{list[9]:>4d}')

#Me falto ver como poner los : despues de cada multiplo
'''
Salida:
 python3 tablamult.py
       0   1   2   3   4   5   6   7   8   9
---------------------------------------------
 0     0   0   0   0   0   0   0   0   0   0
 1     0   1   2   3   4   5   6   7   8   9
 2     0   2   4   6   8  10  12  14  16  18
 3     0   3   6   9  12  15  18  21  24  27
 4     0   4   8  12  16  20  24  28  32  36
 5     0   5  10  15  20  25  30  35  40  45
 6     0   6  12  18  24  30  36  42  48  54
 7     0   7  14  21  28  35  42  49  56  63
 8     0   8  16  24  32  40  48  56  64  72
 9     0   9  18  27  36  45  54  63  72  81
'''
