
# <!-- https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-47.php -->


#-----------
# EXERCICI 1
#-----------

# Donada una llista de tuples ,algunes d'elles buides, o siga (). Crear una llista que elimine les lliste buides.
# 
# llista = [ (1,3), (3,5,3), (), (7,2), (), (5,2,1), (45,)]
# llista_nova = [element for element in llista if element]
# print(llista_nova)

#-----------
# EXERCICI 2
#-----------
# Donat la següent llista de noms, crea una llista que indique les posicios d'aquelles paraules que comencen i acaben en la mateixa lletra.
noms = [ 'Antena', 'Arbre', 'Teulat', 'ordinador' ]
posicions = [i for i, (a,*b,c) in enumerate(noms) if a.lower()==c.lower()]  # type: ignore
print(posicions)

#-----------
# EXERCICI 3
#-----------
# Donat la següent llista. 
dades = {'t': [30, 35, 37, 38], 'p': [800, 900, 1200, 1800], 's': [2,4,6,8]}
# crea una llista de la forma:
#  [  (30, 800, 2),  (35, 900, 4),  (37, 1200, 6),  (38, 1800, 8)]
#
# Pista:
# - primer generar una llista de la forma: [[30, 35, 37, 38], [800, 900, 1200, 1800], [2, 4, 6, 8]]

# valors = [v for v in dades.values()]
# print(valors)

# tuples = [k for k in zip(*valors)]
# print(tuples)


#-----------
# EXERCICI 4
#-----------
# A partir del següent diccionari:
# dades = {'temperatura': [30, 35, 37, 38], 'pressio': [800, 900, 1200, 1800]}

# Obtindre la llegüent llista:
# [ 
#   {'temperatura': 30, 'pressio': 800},
#   {'temperatura': 35, 'pressio': 900},
#   {'temperatura': 37, 'pressio': 1200},
#   {'temperatura': 38, 'pressio': 1800}
# ]

# temperatures = dades['temperatura']
# pressions = dades['pressio']
# resultat = []
# for t, p in zip(temperatures,pressions):
#     resultat.append({'temperatura':t, 'pressio':p})


# Fer el mateix, però d'una manera genèrica.
# dades = {'temperatura': [30, 35, 37, 38], 'pressio': [800, 900, 1200, 1800], 'temps': [2,4,6,8]}

# valors = [v for v in dades.values()]
# print(valors)

# tuples = [k for k in zip(*valors)]
# print(tuples)

# llista = [dict(zip(dades.keys(), v)) for v in tuples]
# print(llista)