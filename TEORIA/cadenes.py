# Els strings es delimiten per cometes simples o dobles.
# Podem escapar caràcters com \n    \\     \'    \"

# ------------------
# Concatenar strings
# ------------------
s1 = 'hola ' + 'i adeu'
s1 += ' i més text'


# ------------------
# operador *
# ------------------
s2 = 'hola ' * 3  # hola hola hola

# ------------------
# cometes triples per a cadenes multilínia
# ------------------
s3 = ''' Això és una cadena
que ocupa tres
línies'''

# ------------------
# rawdata
# ------------------
s4 = r'abc\n123'  # abc\n123

# ------------------
# Els strings estan indexats
# 	H	O	L	A
# 	0	1	2	3
# 	-4	-3	-2	-1
# ------------------
s5 = 'hola'	 # s5[0]

# ------------------
# Els string són IMMUTABLES
# ------------------
s5[0] = 'x'		# Error, no podem canviar un string

# ------------------
# substrings: [inici, final, increment]
# ------------------
s6 = '0123456789'
print(s6[4:])       # 456789        Descarta els 4 primers
print(s6[:4])       # 0123          Selecciona els 4 primers
print(s6[1:4])      # 123           Selecciona de la posició 1 a la 4-1
print(s6[1:8:2])    # 1357          Selecciona de la posició 1 a la 8-1 de 2 en 2
print(s6[::-1])     # 9876543210    Invertix l'string
print(s6[-8:-2])    # 234567
print(s6[-2:])      # 89            Selecciona els 2 últims caràcters
print(s6[:-2])      # 01234567      Descarta els 2 últims caràcters


# ------------------
# Operador in
# ------------------
print('cad' in 'cadena')  # True

# ------------------
# split: dividir una cadena
# ------------------
s7 = 'Això és una cadena'
# Separador: espai en blanc.	Retorna un List:['Això', 'és', 'una', 'cadena']
print(s7.split())

s8 = '54,34,56,23,53,,34'
print(s8.split(';'))  # Separador: ;	Retorna un List: ['54,34,56,23,53,,34']

# strip: Elimina caràcters inicials i finals d'una cadena.
s9 = '   usuari   '
print(s9.strip())  # usuari		Esborra espais en blanc inicials i finals

s10 = '***<usuari>***'
print(s10.strip('*'))  # <usuari>	Esborra els * inicials i finals

s11 = 'hola\n'
s12 = s11.split('\n')  # Esborra els salts de línia inicials i finals.
print(s12)
print('------')

# ------------------
# startswith, endswith, find: Busca en cadenes
# ------------------
s13 = 'ABCDEF'
print(s13.startswith('AB'))		# True
print(s13.endswith('EF'))		# True

s14 = '---hola----hola---'
# 3		Retorna la posició on comença la 1a ocurrència, -1 si no la troba
print(s14.find('hola'))
print(s14.count('hola'))  # 2		Nombre d'ocurrències, 0 sinó n'hi ha.

# ------------------
# replace: Reemplaçament de cadenes
# ------------------
# replace retorna una 'nova cadena', no modifica l'original.
s15 = 'Això està bé i bé'
print(s15.replace('bé', 'malament'))		# Això està malament i malament.

# Podem indicar el nombre d'ocurrències a canviar
print(s15.replace('bé', 'malament', 1))		# Això està malament i bé

#
# ------------------
# capitalize, title, upper, lower: Majúscules i minúscules
# ------------------
s16 = 'Antonio José'
print(s16.capitalize())     # Antonio josé		Posa la 1a lletra en majúscula
# Antonio José		Posa en majúscula la 1a lletra de cada paraula
print(s16.title())
print(s16.upper())          # ANTONIO JOSÉ		Pasa a majúscules tota la cadena
print(s16.lower())          # antonio josé		Pasa a minúscules tota la cadena

# isalnum, isnumeric, isalpha, isupper, islower,istitle: Identificació de caràcters
print('C3-PO'.isalnum())  # False     Tots els caràcters són nombres o lletres?
print('314'.isnumeric())    # True      Tots els caràcters són nombres?
print('a-b-c'.isalpha())    # False     Tots els caràcters són lletres?
print('B16'.isupper())		# True   	Tots els caràcters són majúscules?
print('small'.islower())  # True      Tots els caràcters són minúscules?
# True   És la 1a lletra de cada paraula majúscula?
print('First Heading'.istitle())
