#Ejercicio 1.11 Bonus de Hipoteca
#Por Valentin Mengascini
# hipoteca.py

#Variables:
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

while saldo > pago_mensual:
    if mes in range(pago_extra_mes_comienzo, (pago_extra_mes_fin+1)):
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado = total_pagado + (pago_mensual + pago_extra)
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes += 1
    print(mes, round(total_pagado, 2), round(saldo, 2))

if pago_mensual > saldo:
    saldo = saldo * (1+tasa/12)
    total_pagado = total_pagado + saldo
    saldo = 0
    mes += 1
    print(mes, round(total_pagado, 2), round(saldo, 2))

print("Total pagado:", round(total_pagado, 2),"\n", "Meses:", mes)
