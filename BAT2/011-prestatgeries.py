from typing import Tuple

# llibre1 = {
#     'isbn': 'MAT001',
#     'titol': 'Integrals indefinides'
# }

# llibre2 = {
#     'isbn': 'MAT002',
#     'titol': 'Logaritmes'
# }


# estant1 = {
#     'capacitat':3,
#     'llibres': [llibre1, llibre2]
# }



# prestatgeria1 = {
#     'id' : 1,
#     'estants': [estant1]
# }

# prestatgeria2 = {
#     'id' : 2,
#     'estants': []
# }


# biblioteca = [prestatgeria1, prestatgeria2]


biblioteca: list[dict] = []
llibres_sense_ubicar: list[dict] = []
estants_sense_ubicar: list[dict] = []

# --------------------------------------------
def isbn_correcte(isbn:str)->bool:
    '''
        Un ISBN sempre té 3 lletres en majúscula seguit de 3 dígits. Per exemple: MAT002
    '''
    if len(isbn) != 6:
        return False
    return isbn[:3].isalpha() and isbn[3:].isdigit()

def crea_llibre()-> Tuple[bool,dict]:
    '''
        Retorna True i el llibre si el llibre s'ha creat.
        Retorna False i {} sinó s'ha creat (Intro per a eixir).
    '''
    while True:
        print('Introduïx un ISBN o Intro per a eixir')
        isbn = input('ISBN? ')
        if not isbn.strip():
            return False, {}
        if isbn_correcte(isbn):
            break
        print('Error, ISBN incorrecte')
    
    print('Introduïx el nom del llibre')
    nom = input('Nom? ')
    return True, {'isbn':isbn, 'titol':nom}

# --------------------------------------------
def capacitat_estant_correcta(capacitat: int)->bool:
    '''
        La capacitat d'un estant està entre 0 i 10
    '''
    return capacitat>=0 and capacitat<=10

def crea_estant()-> Tuple[bool,dict]:
    '''
        Crea un nou estant. La capacitat ha de complir la restricció.
        Retorna False i {} si no hem creat l'estant (Intro per a eixir).
        Retorna True i el nou estant.
    '''
    while True:
        try:
            print('Introduïx la quantita de llibres màxima o Intro per a eixir')
            capacitat = input('Capacitat? ')  
            if not capacitat.strip():
                return False, {}
            capacitat_int = int(capacitat)
            if capacitat_estant_correcta(capacitat_int):
                return True, {'capacitat':capacitat_int, 'llibres':[]}
            print('Error: capacitat fóra de límits')
        except ValueError:
            print('Error: capacitat incorrecta')
  

# --------------------------------------------
def afig_estant(prestatgeria: dict) -> Tuple[bool, str]:
    '''
        No hi ha límit d'estants que es pot afegir a una estanteria.
        Agafa un dels estants de la llista estants_sense_ubicar.
        Retorna True i '' si s'ha afegit l'estant a la prestatgeria.
        Retorna Fase i un missatge d'error si no s'ha afegit.
            El codi d'error és 'No queden estant nous per ubicar'
    '''
    try:
        estant = estants_sense_ubicar.pop()
    except IndexError:
        return False, 'No queden estant nous per ubicar'
    
    prestatgeria['estants'].append(estant)

    return True, ''

# --------------------------------------------
def obtin_prestatgeria(id: int) -> Tuple[bool, dict]:
    '''
        Si l'identificador de la prestatgeria és correcte retorna True i la prestatgeria.
        Si l'identificador no existix retorna False i {}
    '''
    for prestatgeria in biblioteca:
        if prestatgeria['id']==id:
            return True, prestatgeria
    return False, {}



def nombre_llibres(estant: dict) -> int:
    '''
        Retorna el nombre de llibre de l'estant que li passem.
    '''
    return len(estant['llibres'])
    

def afig_llibre(prestatgeria: dict, llibre: dict) -> Tuple[bool, str]:
    '''
        Retorn True i '' si s'ha afegit el llibre al codi d'estanteria indicada.
        Retorna False i un missatge d'error si no s'afegit. Els errors són:
            'Prestatgeria plena, afig un nou estant'
    '''
   
    for estant in prestatgeria['estants']:
        if nombre_llibres(estant) + 1 < estant['capacitat']:
            estant['llibres'].append(llibre)
            return True, ''

    return False, 'Prestatgeria plena, afig un nou estant'


def demana_usuari_prestatgeria() -> Tuple[bool, dict]:
    '''
        Demana a l'usuari que introduixa el codi d'una prestatgeria.
        Retorna True i la prestatgeria si s'ha introduit un codi vàlid
        Retorna False i {} si no s'ha introduït (Intro per a eixir)
    '''
    while True:
        try:
            print("Introduïx l'identificador d'una prestatgeria o Intro per a eixir")
            id = input('Identificador? ')
            if not id.strip():
                return False, {}
            id_int = int(id)
            existix, prestatgeria = obtin_prestatgeria(id_int)
            if existix:
                return True, prestatgeria
            print('Error, la prestatgeria no existix')
        except ValueError:
            print('Error, codi incorrecte')


def demana_usuari_isbn_llibre_sense_ubicar() -> Tuple[bool, dict]:
    '''
        Demana a l'usuari que introduixa l'isbn d'un llibre de la llista de llibres sense ubicar o Intro per a continuar.
    '''
    while True:
        print("Introduïx l'isbn d'un llibre sense ubicar o Intro per a eixir")
        isbn = input('ISBN? ')
        if not isbn.strip():
            return False, {}
        
        for llibre in llibres_sense_ubicar:
            if llibre['isbn']==isbn:
                return True, llibre
        
        print('Error: Este isbn no està en la llista de llibres sense ubicar')

# --------------------------------------------
def obtin_nou_codi_prestatgeria() -> int:
    return len(biblioteca) + 1


def crea_i_afig_una_prestatgeria_a_la_biblioteca() -> None:
    id = obtin_nou_codi_prestatgeria()
    nova_prestatgeria = { 'id':id, 'estants':[]}
    biblioteca.append(nova_prestatgeria) 




msg_error = ''

while True:
    print(f'\nBiblioteca : {biblioteca}')
    print(f'Llibres sense ubicar {llibres_sense_ubicar}')
    print(f'estants sense ubicar {estants_sense_ubicar}')
    print('--- MENÚ ---')
    print('1- Afig una estanteria nova a la biblioteca')
    print('2- Crea un llibre nou')
    print('3- Crea un estant nou')
    print('4- Afig un estant a una prestatgeria')
    print('5- Afig un llibre a una prestatgeria')
    print('6- Busca i lleva un llibre de la biblioteca')
    print('Q- Ix del programa')


    opcio = input('Opció? ')
    if opcio == '1':
        crea_i_afig_una_prestatgeria_a_la_biblioteca()
    elif opcio == '2':
        llibre_creat, llibre = crea_llibre()
        if llibre_creat:
            llibres_sense_ubicar.append(llibre)
    elif opcio == '3':
        estant_creat, estant = crea_estant()
        if estant_creat:
            estants_sense_ubicar.append(estant)
    elif opcio == '4':
        correcte, prestatgeria = demana_usuari_prestatgeria()
        if correcte:
            estant_afegit, msg_error = afig_estant(prestatgeria)
    elif opcio == '5':
        correcte, llibre = demana_usuari_isbn_llibre_sense_ubicar()
        if correcte:
            correcte, prestatgeria = demana_usuari_prestatgeria()
            if correcte:
                correcte, msg_error= afig_llibre(prestatgeria, llibre)
    elif opcio == 'Q':
        exit()
    else:
        print('ERROR: Opció incorrecta')
    
    print(msg_error)
    msg_error = ''
