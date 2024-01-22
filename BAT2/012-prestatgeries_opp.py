# from typing import Tuple

# --------------------------------------------
class Isbn_incorrecte(Exception):
    pass

class Prestatgeria_sense_estants(Exception):
    pass 

class Prestatgeria_plena(Exception):
    pass

class Llibre_no_esta_en_biblioteca(Exception):
    pass


# --------------------------------------------
class Llibre:
    def __init__(self, isbn:str, titol:str) -> None:
        self.isbn = isbn
        self.titol = titol
    
    @classmethod
    def isbn_correcte(cls, isbn:str) -> bool:
        return len(isbn) == 6 and isbn[:3].isalpha() and isbn[3:].isdigit()
    
    def __str__(self) -> str:
        return f'Llibre {self.isbn}, {self.titol}'
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj, Llibre):
            return self.isbn == obj.isbn
        return False

# --------------------------------------------
class Estant:
    def __init__(self, capacitat:int) -> None:
        self.capacitat:int = capacitat
        self.llibres:list[Llibre] = []

    def nombre_llibres(self) -> int:
        return len(self.llibres)

    @classmethod
    def capacitat_correcta(cls, capacitat:int) -> bool:
        return capacitat>=0 and capacitat<=10
    
    def __str__(self) -> str:
        cadena = f' Estant de {self.capacitat} llibres'
        for llibre in self.llibres:
            cadena += ', ' + llibre.isbn
        return cadena
# --------------------------------------------
class Prestatgeria:
    def __init__(self) -> None:
        global biblioteca
        self.estants:list[Estant] = []
        self.id = biblioteca.nombre_prestatgeries + 1

    def afig_estant(self) -> None:
        estant = estants_sense_ubicar.pop()
        self.estants.append(estant)

    def afig(self, llibre: Llibre):
        if not self.estants:
            raise Prestatgeria_sense_estants
        
        for estant in self.estants:
            if estant.nombre_llibres() < estant.capacitat:
                estant.llibres.append(llibre)
                return
 
        raise Prestatgeria_plena
    
# --------------------------------------------
class Biblioteca:
    def __init__(self) -> None:
        self.prestatgeries: list[Prestatgeria] = []

    def afig(self, prestatgeria: Prestatgeria) -> None:
        self.prestatgeries.append(prestatgeria)

    @property
    def nombre_prestatgeries(self) -> int:
        return len(self.prestatgeries)

    def obtin(self, id_prestatgeria: int) -> Prestatgeria|None:
        for prestatgeria in self.prestatgeries:
            if prestatgeria.id == id_prestatgeria:
                return prestatgeria
        return None
    



llibre1 = Llibre(isbn='aaa111', titol='aaa')
llibre2 = Llibre(isbn='bbb222', titol='bbb')
estant1 = Estant(2)

biblioteca = Biblioteca()
llibres_sense_ubicar: list[Llibre] = [llibre1, llibre2]
estants_sense_ubicar: list[Estant] = [estant1]


# --------------------------------------------
def crea_i_afig_una_prestatgeria_a_la_biblioteca() -> None:
    prestatgeria = Prestatgeria()
    biblioteca.afig(prestatgeria)

# --------------------------------------------
def crea_llibre() -> Llibre|None:
    while True:
        print('Introduïx un ISBN o Intro per a eixir')
        isbn = input('ISBN? ')
        if not isbn:
            return None
        if Llibre.isbn_correcte(isbn):
            break
        print('Error, ISBN incorrecte')
    
    print('Introduïx el nom del llibre')
    nom = input('Nom? ')
    return Llibre(isbn, nom)

# --------------------------------------------
def crea_estant()-> Estant|None:
    while True:
        try:
            print('Introduïx la quantitat de llibres màxima o Intro per a eixir')
            capacitat = input('Capacitat? ')
            if not capacitat:
                return None
            capacitat_int = int(capacitat)
            if Estant.capacitat_correcta(capacitat_int):
                return Estant(capacitat_int)
        except ValueError:
            print('Error: capacitat fóra de límits')

# --------------------------------------------
def demana_usuari_prestatgeria() -> Prestatgeria|None:
    while True:
        try:
            print("Introduïx l'identificador d'una prestatgeria o Intro per a eixir")
            id_prestatgeria = input('Identificador? ')
            if not id_prestatgeria:
                return None
            id_prestatgeria_int = int(id_prestatgeria)
            prestatgeria = biblioteca.obtin(id_prestatgeria_int)
            if prestatgeria:
                return prestatgeria
            print('Error, la prestatgeria no existix')
        except ValueError:
            print('Error, codi incorrecte')       

# --------------------------------------------
def demana_usuari_isbn_llibre_sense_ubicar() -> Llibre|None:
    while True:
        print("Introduïx l'isbn d'un llibre sense ubicar o Intro per a eixir")
        isbn = input('ISBN? ')
        if not isbn:
            return None
        
        for llibre in llibres_sense_ubicar:
            if llibre.isbn == isbn:
                return llibre


# --------------------------------------------
# TO DO igualtat
def lleva_llibre_llista_llibres_sense_ubicar(llibre_a_llevar: Llibre) -> None:
    #  for index, llibre in enumerate(llibres_sense_ubicar):
    #         if llibre.isbn == llibre_a_llevar.isbn:
    #             llibres_sense_ubicar.pop(index)
    #             return
    try:
        index = llibres_sense_ubicar.index(llibre_a_llevar)
        llibres_sense_ubicar.pop(index)
    except ValueError:
        pass

# --------------------------------------------
def demana_usuari_isbn() -> str|None:
    while True:
        print("Introduïx l'isbn del llibre a extraure")
        isbn = input('ISBN? ')
        if not isbn:
            return None
        if Llibre.isbn_correcte(isbn):
            return isbn
        print('Error, codi ISBN incorrecte')

# --------------------------------------------
def busca_llibre_i_lleva_de_biblioteca(isbn:str) -> None:
    for prestatgeria in biblioteca.prestatgeries:
        for index,estant in enumerate(prestatgeria.estants):
            for llibre in estant.llibres:
                if llibre.isbn==isbn:
                    llibres_sense_ubicar.append(llibre)
                    estant.llibres.pop(index)
                    return
    raise Llibre_no_esta_en_biblioteca


# --------------------------------------------
def info():
    print('Llibres sense ubicar')
    for llibre in llibres_sense_ubicar:
        print(f'  {llibre}')

    print('\nEstants sense ubicar')
    for estant in estants_sense_ubicar:
        print(f'   {estant}')

    print('\nPrestatgeries')
    for prestatgeria in biblioteca.prestatgeries:
        print(f"  {prestatgeria.id=}")
        for estant in prestatgeria.estants:
            print(f'    {estant}')

msg_error = ''

while True:
    info()
    print('--- MENÚ ---')
    print('1- Afig una prestatgeria nova a la biblioteca')
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
        llibre = crea_llibre()
        if llibre:
            llibres_sense_ubicar.append(llibre)
    elif opcio == '3':
        estant = crea_estant()
        if estant:
            estants_sense_ubicar.append(estant)
    elif opcio == '4':
        prestatgeria = demana_usuari_prestatgeria()
        if prestatgeria:
            if not estants_sense_ubicar:
                msg_error = 'No queden estants nous per ubicar'
            else:
                prestatgeria.afig_estant()
    elif opcio == '5':
        llibre = demana_usuari_isbn_llibre_sense_ubicar()
        if llibre:
            prestatgeria = demana_usuari_prestatgeria()
            if prestatgeria:
                try:
                    prestatgeria.afig(llibre)
                    lleva_llibre_llista_llibres_sense_ubicar(llibre)
                except Prestatgeria_sense_estants:
                    msg_error = 'La prestatgeria no té estants'
                except Prestatgeria_plena:
                    msg_error = 'La prestatgeria està plena'               
    elif opcio == '6':
        try:
            isbn = demana_usuari_isbn()
            if isbn:
                busca_llibre_i_lleva_de_biblioteca(isbn)
        except Llibre_no_esta_en_biblioteca:
            msg_error = 'El llibre no esté es la biblioteca'
    elif opcio == 'Q':
        exit()
    else:
        msg_error = 'ERROR: Opció incorrecta'
    
    print(' --------------------------- ')
    print(f'ERROR: {msg_error}')
    msg_error = ''
