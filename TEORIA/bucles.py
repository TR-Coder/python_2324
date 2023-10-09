#
# En python els bucles s'implemente amb les setències while i for.
#


#============================
# while
#============================
# while expressió_boolena:
#   bloc_sentències
#
# break: acaba el bucle, el flux d'execució continua en la sentència de després del while.
# continue: inicia una nova iteració.
#
#
# while expressió_boolena:
#   bloc_sentències
# else:
#   bloc_sentències         L'else només s'executa si el bucle acaba normalment, o siga que no acaba per un break.
#
#
# Bucle infinit
# While True:
#   bloc_sentències
#


#============================
# for
#============================
# Un for itera sobre un objecte que té la capacitat de ser recorregut: llistes, strings, tuples, conjunts, diccionaris, etc.
# Un objecte té la capacitat de ser recorregut si implementa el mètode iter().
# Quan cridem al mètode iter() retorna un iterador. Com vorem, a través de l'iterador som capaços d'obtindre cada element
# de l'iterable.
# El for, en cada iteració, crida a l'iterador de l'objecte que estem recorrent, i este retorna el següent element.
#
for cadena in ('primer', 'segon', 'tercer'):
    print(cadena)

for nombre in (5,8,4,-1):
    print(nombre)

for caracter in 'HOLA':
    print(caracter)

#
# Recórrer un rang de nombres utilitzem range(valor_inicial, valor_final, increment)
# valor_inicial i valor_final són enter possitius, increment és un enter possitiu o negatiu.
# valor_inicial no entra en l'última iteració.
# 
for i in range(2,10,2):
    print(i)                # 2 4 6 8 (el 10 no entra)

for i in range(12,5,-1):
    print(i)                # 10 9 8 7 6 (el 5 no entra)