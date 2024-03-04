from __future__ import annotations
import datetime as dt
import os
import platform
from dataclasses import dataclass
import pickle

class pelicula_no_trobada(Exception):
    pass
class sessio_no_trobada(Exception):
    pass
class sala_no_trobada(Exception):
    pass
class cine_no_trobat(Exception):
    pass
class input_type_cancel·lat(Exception):
    pass

#==========================================================================================================
pel_licules:list[Pel_licula] = []
cines:list[Cine] = []

#==========================================================================================================
def cls(txt:str|None=None):
    comando = 'cls' if platform.system()=='Windows' else 'clear'
    os.system(comando)
    if txt:
        print(txt)

#==========================================================================================================
class Reserva:
    def __init__(self, dni:str) -> None:
        self.dni = dni

    def __str__(self) -> str:
        return self.dni
    
    __repr__ = __str__

#==========================================================================================================
class Pel_licula:
    id:int = 1
    def __init__(self, info:str) -> None:
        self.id = Pel_licula.id
        Pel_licula.id += 1
        self.info = info

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Pel_licula):
            return False
        return obj.id==self.id

#==========================================================================================================
class Cine:
    id:int = 1
    def __init__(self, descripcio:str) -> None:
        self.id = Cine.id
        Cine.id += 1
        self.descripcio = descripcio
        self.sales:list[Sala] = []

    def busca_sala(self, id_sala:int) -> Sala:
        for sala in self.sales:
            if sala.id == id_sala:
                return sala
        raise sala_no_trobada

#==========================================================================================================
class Sala:
    id:int = 1
    def __init__(self, cine: Cine, descripcio:str, files: int, seients_per_fila:int) -> None:
        self.id = Sala.id
        Sala.id += 1
        self.descripcio = descripcio
        self.files = files
        self.seients_per_fila = seients_per_fila
        self.sessions:list[Sessio] = []
        cine.sales.append(self)
    
    def busca_sessio(self, id_sessio: int) -> Sessio:
        for sessio in self.sessions:
            if sessio.id==id_sessio:
                return sessio
        raise sessio_no_trobada

#==========================================================================================================
class Sessio:
    id:int = 1
    def __init__(self, sala:Sala, data_hora:dt.datetime, pel_licula:Pel_licula, preu_entrada:float) -> None:
        self.id = Sessio.id
        Sessio.id += 1
        self.data_hora:dt.datetime = data_hora
        self.pel_licula = pel_licula
        self.preu_entrada = preu_entrada
        self.reserves:list[list[Reserva|None]] = [[None] * sala.seients_per_fila for _ in range(sala.files)]
        sala.sessions.append(self)
    
    def mostra_reserves(self) -> None:
        for i, fila in enumerate(self.reserves):
            print(f'fila {i}: {fila}')

#------------------------------------------------------------------------
def obtin_data() -> dt.date|None:
    while True:
        try:
            d = input('Si vols, introduïx un data (ddmmaa)')
            if d=='':
                return None
            return dt.datetime.strptime(d, '%d%m%y').date()
        except ValueError:
            print('Data incorrecta')

#------------------------------------------------------------------------
def obtin_data_hora() -> dt.datetime:
    while True:
        try:
            ddmmaa = input_type('Introduïx un data (ddmmaa)', 'str')
            data = dt.datetime.strptime(ddmmaa, '%d%m%y')                # type: ignore
            hhmm = input_type('Introduce una hora (hhmm)', 'str')
            hora = dt.datetime.strptime(hhmm, "%H%M").time()           # type: ignore
            return dt.datetime.combine(data, hora)
        except ValueError:
            print('Data incorrecta')

#==========================================================================================================
# Manteniment de pel·lícules
#==========================================================================================================
def menu_pel_licules() -> None:
    while True:
        try:
            cls('- LLISTA DE PEL·LÍCULES -')
            mostra_pel_licules()      
            opc = input('(Intro=Eixir) 1-Crea, 2-Modifica, 3-Esborra. Opció? ')
            if opc=='':
                return
            elif opc=='1':
                crea_pel_licula()
            elif opc=='2':
                modifica_pel_licula()
            elif opc =='3':
                esborra_pel_licula()
            else:
                print('Opció incorrecta')
        except input_type_cancel·lat:
            continue

#------------------------------------------------------------------------
def mostra_pel_licules() -> None:
    if not pel_licules:
        print(' No hi ha pel·licules')
        return
    
    for pel_licula in pel_licules:
        print(f'{pel_licula.id} {pel_licula.info}')
    print()

#------------------------------------------------------------------------
def crea_pel_licula() -> None:
    print("CREACIÓ D'UNA PEL·LÍCULA:")
    while True:
        descripcio = input_type('Descripció de la pel·lícula')  
        pel_licula = Pel_licula(descripcio)                     # type: ignore
        pel_licules.append(pel_licula)
        grava_arxiu()
        print('Fet')
        return

#------------------------------------------------------------------------
def busca_pel_licula(id: int) -> Pel_licula:
    for pel_licula in pel_licules:
            if pel_licula.id==id:
                return pel_licula
    raise pelicula_no_trobada

#------------------------------------------------------------------------
def demana_pel_licula(txt:str) -> Pel_licula:
    while True:       
        try:
            id = input_type(txt,'int')           # type: ignore
            pel_licula = busca_pel_licula(id)    # type: ignore
            return pel_licula
        except pelicula_no_trobada:
            print('Error: Id de la pel·lícula incorrecte')

#------------------------------------------------------------------------
def modifica_pel_licula() -> None:
    print("MODIFICACIÓ D'UNA PEL·LÍCULA:")
    pel_licula = demana_pel_licula('Id de la pel·lícula a modificar')
    info = input('Nova descripció? ')
    pel_licula.info = info
    grava_arxiu()
    print('Fet')

#------------------------------------------------------------------------
def esborra_pel_licula():
    print("ESBORRAT D'UNA PEL·LÍCULA:")
    pel_licula = demana_pel_licula('Id de la pel·lícula a esborrar')
    pel_licules.remove(pel_licula)
    grava_arxiu()
    print('Fet')

#------------------------------------------------------------------------
def input_type(text:str, type:str='str', excepcio:bool=True, intro_cancellar:bool=True) -> int|str|float|None:
    while True:
        try:
            txt_intro = '(Intro=cancel·lar) ' if intro_cancellar else ''
            cadena = input(f'{txt_intro}{text} ')
            if cadena=='':
                if excepcio:
                    raise input_type_cancel·lat
                return ''
            elif type=='int':
                return int(cadena)
            elif type=='str':
                return cadena
            elif type=='float':
                return float(cadena)
        except ValueError:
            print('Valor incorrecte')

#==========================================================================================================
# Reserves
#==========================================================================================================
def busca_cine(id: int) -> Cine:
    for cine in cines:
        if cine.id==id:
            return cine
    raise cine_no_trobat           

#------------------------------------------------------------------------
def mostra_cine_i_sales() -> None:
    for cine in cines:
        print('---------------------------------')
        print(f'CINE: {cine.id} {cine.descripcio}')
        for sala in cine.sales:
            print(f'   SALA {sala.id} {sala.descripcio}')
    print()

#------------------------------------------------------------------------
def selecciona_cine() -> Cine:
    cls('- LLISTA DE CINES -')
    if not cines:
        input(' No hi ha cines. Intro per a continuar')
        raise input_type_cancel·lat
    mostra_cine_i_sales()   
    while True:
        try: 
            id_cine = input_type('Selecciona un cine:', 'int')
            cine = busca_cine(id_cine)                                  # type: ignore
            return cine
        except cine_no_trobat:
            print('Id del cine incorrete')

#------------------------------------------------------------------------
def mostra_sales_i_sessions(cine:Cine) -> None:
    print(f'Cine: {cine.id} {cine.descripcio}')                         # type: ignore
    for sala in cine.sales:
        print('   ---------------------------------')                   # type: ignore
        print(f'   SALA: {sala.id} {sala.descripcio}')
        if not sala.sessions:
            print('        No hi ha sessions')
            continue
        for sessio in sala.sessions:
            print(f"       SESSIÓ {sessio.id}: {sessio.data_hora.strftime('%d/%m/%y %HH:%MM')} {sessio.pel_licula.info} {sessio.preu_entrada}")
    print()

#------------------------------------------------------------------------
def demana_sala(cine:Cine) -> Sala:
    id_sala = input_type('Selecciona una sala:', 'int')
    sala = cine.busca_sala(id_sala)                    # type: ignore
    return sala

#------------------------------------------------------------------------
def demana_sessio(sala:Sala) -> Sessio:
    id_sessio = input_type('Selecciona una sessió:', 'int')
    sessio = sala.busca_sessio(id_sessio)              # type: ignore
    return sessio

#------------------------------------------------------------------------
def demana_seient(sala:Sala, sessio:Sessio) -> tuple[int,int]:
    while True:
        fila:int = input_type('Fila:','int')            # type: ignore

        if fila<0 or fila>sala.files-1:
            print('Error, fila incorrecta')
            continue

        seient:int = input_type('Seient:', 'int')       # type: ignore
        if seient<0 or seient>sala.seients_per_fila-1:
            print('Error, seient incorrecte')
            continue

        return fila, seient
    
#==========================================================================================================
# Manteniment de sessions
#==========================================================================================================
def manteniment_sessions(cine:Cine) -> None:  
    cls('- LLISTA DE SALES I SESSIONS -')
    mostra_sales_i_sessions(cine)
    while True:
        try:
            sala = demana_sala(cine)
            print(f'Manteniment de sessions de la sala: {sala.id} {sala.descripcio}')
            opc = input_type('1-crea, 2-Modifica, 3-Esborra, 4=Reserves. Opció?', excepcio=False)
            if opc=='':
                pass
            elif opc=='1':
                crea_sessio(sala)
            elif opc=='2':
                modifica_sessio(sala)
            elif opc=='3':
                esborra_sessio(sala)
            elif opc=='4':
                mateniment_reserves(cine, sala)
        except input_type_cancel·lat:
            break
        except sala_no_trobada:
            print('Sala incorrecta')
        except sessio_no_trobada:
            print('Sessió incorrecta')
        else:
            cls('- LLISTA DE SALES I SESSIONS -')
            mostra_sales_i_sessions(cine)

 
#------------------------------------------------------------------------
def demana_dades_reserva() -> Reserva:
    dni:str = input_type('DNI per a la reserva:')       # type: ignore
    return Reserva(dni)

#------------------------------------------------------------------------
def mateniment_reserves(cine:Cine, sala:Sala) -> None:
    while True:
        cls('- LLISTA DE RESERVES -')
        print(f'cine {cine.id} {cine.descripcio}')
        print(f'Sala {sala.id} {sala.descripcio}')
        print()
        for sessio in sala.sessions:
            print(f'SESSIÓ {sessio.id} {sessio.data_hora} {sessio.preu_entrada}')
            sessio.mostra_reserves()
        try:
            opc = input_type('1-Modifica reserva:')
            if opc=='1':
                fila, seient = demana_seient(sala, sessio)
                if sessio.reserves[fila][seient]:
                    valor:str = input(f'Eliminar la reserva {fila},{seient} (S/ )? ')   
                    if valor.upper()=='S':
                        sessio.reserves[fila][seient] = None
                        grava_arxiu()
                else:
                    valor = input(f'Reservar {fila},{seient} (S/ )? ')                 
                    if valor.upper()=='S':
                        reserva = demana_dades_reserva()
                        sessio.reserves[fila][seient] = reserva
                        grava_arxiu()
        except input_type_cancel·lat:
            return

#------------------------------------------------------------------------
def crea_sessio(sala:Sala) -> None:
    print("CREACIÓ D'UNA SESSIÓ:")
    while True:
        try:
            data_hora = obtin_data_hora()
            pel_licula = demana_pel_licula('Id de la pel·lícula') 
            preu:float = input_type("Preu de l'entrada", 'float')       # type: ignore
            Sessio(sala, data_hora, pel_licula, preu)
            grava_arxiu()
            input('Fet. Intro per a continuar')
            return
        except input_type_cancel·lat:
            return
#------------------------------------------------------------------------
def modifica_sessio(sala:Sala) -> None:
    print("MODIFICACIÓ D'UNA SESSIÓ:")
    while True:
        try:
            sessio = demana_sessio(sala)
            data_hora = obtin_data_hora()
            pel_licula = demana_pel_licula('Id de la pel·lícula') 
            preu:float = input_type("Preu de l'entrada", 'float')       # type: ignore
            sessio.data_hora = data_hora
            sessio.pel_licula = pel_licula
            sessio.preu_entrada = preu
            grava_arxiu()
            input('Fet. Intro per a continuar')
            return
        except input_type_cancel·lat:
            return
        except sessio_no_trobada:
            print('Sessió incorrecta')

#------------------------------------------------------------------------
def esborra_sessio(sala:Sala) -> None:
    print("ESBORRAT D'UNA SESSIÓ")
    while True:
        try:
            sessio = demana_sessio(sala)
            sala.sessions.remove(sessio)
            grava_arxiu()
            input('Fet. Intro per a continuar')
            return
        except input_type_cancel·lat:
            return
        except sessio_no_trobada:
            print('Sessió incorrecta')

#==========================================================================================================
# Reserva d'una pel·lícula
#==========================================================================================================
#==========================================================================================================
@dataclass
class Resultat:
    cine: Cine
    sala: Sala
    sessio: Sessio

#------------------------------------------------------------------------
def busca_sessions_on_vore_pel_licula(pel_licula:Pel_licula, data_hora:dt.date|None=None) -> list[Resultat]:
    ''' Recorre els cines i les seues sales buscant aquelles sessions on es projecta una pelicula determinana, de manera 
        opcional també es pot buscar en una data concreta.'''
    filtre:list[Resultat] = []
    for cine in cines:
        for sala in cine.sales:
            for sessio in sala.sessions:
                if  (sessio.pel_licula==pel_licula) and \
                    (not data_hora or data_hora and data_hora==sessio.data_hora.date()):
                    filtre.append(Resultat(cine,sala,sessio))
    if not filtre:
        raise pelicula_no_trobada
    return filtre

#------------------------------------------------------------------------
def selecciona_sessio_on_vore_pel_licula(pel_licula:Pel_licula, data:dt.date|None) -> tuple[Sala,Sessio]:
    filtre:list[Resultat] = busca_sessions_on_vore_pel_licula(pel_licula, data)
    for item in filtre:
        print(f'CINE: {item.cine.descripcio}, {item.sala.descripcio}. SESSIÓ: {item.sessio.id}, {item.sessio.data_hora}')

    while True:
        id_sessio = input_type('Selecciona una sessió:','int')
        for item in filtre:
            if item.sessio.id==id_sessio:
                return item.sala, item.sessio
        print('Sessió incorrecta')

#------------------------------------------------------------------------
def reserva_pel_licula() -> None:
    ''' Seleccionem una pel·lícula.
        Seleccionar un día.
        Mostrar el cine, les sales i les sessions on podem reservar la pel·lícula.
        Fer la reserva en la sessió seleccionada
    '''
    while True:
        try:
            cls("- RESERVA D'UNA PEL·LÍCULA -")
            mostra_pel_licules()
            pel_licula = demana_pel_licula('Id de la pel·lícula que vols vore')
            data = obtin_data()
            sala,sessio = selecciona_sessio_on_vore_pel_licula(pel_licula, data)
            reserva_pel_licula_en_sessio(sala, sessio)
        except pelicula_no_trobada:
            input('No hi ha sessions per a la película i data seleccionades')
            continue
        except input_type_cancel·lat:
            return

#------------------------------------------------------------------------
def reserva_pel_licula_en_sessio(sala:Sala, sessio:Sessio) -> None:
    while True:
        try:
            sessio.mostra_reserves()
            fila, seient = demana_seient(sala, sessio)
            if sessio.reserves[fila][seient]:
                print('Error, el seient ja està reservat')
                continue
            reserva = demana_dades_reserva()
            sessio.reserves[fila][seient] = reserva
            grava_arxiu()
            print('Reserva feta')
        except input_type_cancel·lat:
            return
    
#==========================================================================================================
def grava_arxiu() -> None:
    with open('arxiu.pkl', 'wb') as fd:
        pickle.dump(pel_licules, fd)
        pickle.dump(cines, fd)


def llig_arxiu() -> None:
    global pel_licules
    global cines
    if not os.path.exists('arxiu.pkl'):
        grava_arxiu()
        return
    with open('arxiu.pkl', 'rb') as fd:
        pel_licules = pickle.load(fd)
        cines = pickle.load(fd)

#==========================================================================================================
def mostra_menu() -> None:
    while True:
        cls('- MENÚ PRINCIPAL -')
        print('------------------')
        print('1- Cines i sales (no implementat)')
        print('2- Pel·lícules')
        print('3- Sessions')
        print('4- Reserves')
        print()

        try:
            opc = input_type('Opció?', intro_cancellar=False)
            if opc=='1':
                pass                            # Opció no implementada
            elif opc=='2':
                menu_pel_licules()
            elif opc=='3':
                cine = selecciona_cine()
                manteniment_sessions(cine)
            elif opc=='4':
                reserva_pel_licula()
        except input_type_cancel·lat:
            continue

#==========================================================================================================
# Per a simplificar el programa assumirem que els cines amb les sales estan creats.
        
# p1 = Pel_licula('La guerra de les galaxies')
# p2 = Pel_licula('Jocs de guerra')
# p3 = Pel_licula('Encontres en la 3a fase')
# p4 = Pel_licula('Indiana Jones')

# pel_licules.append(p1)
# pel_licules.append(p2)
# pel_licules.append(p3)
# pel_licules.append(p4)

# c1 = Cine('La salera')
# cines.append(c1)

# sala1 = Sala(c1, 'sala 1', 3, 4)
# sala2 = Sala(c1, 'sala 2', 2, 5)

# data1= dt.datetime(2024, 1, 1, 12, 0, 0)
# data2= dt.datetime(2024, 1, 1, 14, 0, 0)
# data3= dt.datetime(2024, 1, 1, 16, 0, 0)

# sessio1 = Sessio(sala1,data1,p1,5)
# sessio2 = Sessio(sala1,data2,p1,6)


if __name__ == "__main__":
    llig_arxiu()
    mostra_menu()