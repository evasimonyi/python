# konzolra a számokat 1-től 100-ig úgy, hogy ha a szám osztható 3-mal, akkor azt írod a szám helyett, hogy "Piff", ha osztható 7-tel, akkor azt, hogy "Puff", ha mindkettővel, akkor pedig azt, hogy "PiffPuff".

for i in range(1, 101):
    if i % 3 == 0 and i % 3 == 0:
        print('PiffPuff')
    elif i % 3 == 0:
        print('Piff')
    elif i % 7 == 0:
        print('Puff')
    else:
        print(i)
