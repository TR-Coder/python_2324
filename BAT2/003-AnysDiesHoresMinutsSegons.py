
# ====================
# ENUNCIAT A
# ====================
# Passar de segons a anys, dies, hores, minuts i segons. EXEMPLE:
#
#   300.000 segons són 3 díes, 11 hores, 20 minuts i 0  segons.
#   7.400   segons són 0 díes, 2  hores, 3  minuts i 20 segons.
#
# Assumim anys de 365 dies.



# ====================
# TEORIA
# ====================
# Per a eliminar la part decimal:
#   int(variable)
#   math.trunc(variable)

# No val:
#   print(f'{variable:.0f}) ja que arredonix.



# SOLUCIÓ A

segons: float = float(input('Introduïx els segons: '))

minuts: float = segons // 60
segons = segons % 60

hores: float = minuts // 60
minuts = minuts % 60

dies: float = hores // 24
hores = hores % 24

anys = dies // 365
dies = dies % 365

print(f'Són {int(anys)} anys, {int(dies)} dies, {int(hores)} hores, {int(minuts)} minuts i {int(segons)} segons')


# SOLUCIÓ B
anys = segons // 31536000
segons %= 31536000
dies = segons // 86400
segons %= 86400
hores = segons // 3600
segons %= 3600
minuts = segons // 60
segons %= 60
print(anys, dies, hores, minuts, segons)



# ====================
# ENUNCIAT B
# ====================
# Ara no assumim anys de 365 dies, poden ser bixestos o no.
# Passar de segons a anys, dies, hores, minuts i segons a partir de l'any 1.970
#
# Nota:
# Un any és bixest si és divisible per 4 i no és divisible per 100.
# Excepció: Tot any divisible per 400 també és bixest.

# Exemple:
# - 2.024 és bixest    perquè és divisible per 4 i no és divisible per 100.
# - 1.900 no és bixest perquè és divisible per 4 i és divisible per 100. Tampoc ho es per 400.
# - 2.000 és bixest    perquè, tot i ser divisible per 4 i divisible per 100 que el faria no bixet, és divisible per 400 que el fa bixest.
# - 200   no és bixest perquè és divisible per 4 i és divisible per 100. Tampoc ho es per 400.


# any_bixest = (any%4 == 0 and any%100 != 0) or (any%400 == 0)
# any bixest té 31.622.400
# any no bixest té 31.536.000

# Any	Segons per any
# 1970	31.536.000
# 1971	31.536.000
# 1972	31.622.400
# 1973	31.536.000
# 1974	31.536.000
# 1975	31.536.000
# 1976	31.622.400
# 1977	31.536.000
# 1978	31.536.000
# 1979	31.536.000
# 1980	31.622.400


segons = 94694_401

segons_per_any = 31_536_000           # 365 dies
segons_per_any_bixest = 31_622_400    # 366 dies

anys = 0
while True:
    any_actual = 1970 + anys
    es_bixest = (any_actual % 4 == 0 and any_actual % 100 != 0) or (any_actual % 400 == 0)
    segons_per_any_actual = segons_per_any_bixest if es_bixest else segons_per_any

    if segons < segons_per_any_actual:
        break

    segons -= segons_per_any_actual
    anys += 1

dies = segons // 86400
segons %= 86400
hores = segons // 3600
segons %= 3600
minuts = segons // 60
segons %= 60

print(anys, dies, hores, minuts, segons)