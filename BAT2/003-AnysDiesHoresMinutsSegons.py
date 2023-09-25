from math import trunc

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

# EXEMPLE
#  300.000 segons són 3 díes, 11 hores, 20 minuts i 0  segons.
#  7.400   segons són 0 díes, 2  hores, 3  minuts i 20 segons.


# Per a eliminar la part decimal.
#  int(variable)
#  math.trunc(variable)

# No val:
# print(f'{variable:.0f}) ja que arrodonix.
