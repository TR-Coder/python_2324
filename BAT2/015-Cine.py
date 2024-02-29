from __future__ import annotations
import datetime as dt
import os
import platform
import pickle

class sala_no_trobada(Exception):
    pass
class cine_no_trobat(Exception):
    pass
#==========================================================================================================
pel_licules:list[Pel_licula] = []
cines:list[Cine] = []
cine_actiu:Cine|None = None
sala_activa:Sala|None = None

#==========================================================================================================
def neteja_pantalla():
    comando = 'cls' if platform.system()=='Windows' else 'clear'
    os.system(comando)

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

#==========================================================================================================
class Sessio:
    id:int = 1
    def __init__(self, sala:Sala, data_hora:dt.datetime, pel_licula:Pel_licula, preu_entrada:float) -> None:
        self.id = Sessio.id
        Sessio.id += 1
        self.data_hora:dt.datetime = data_hora
        self.pel_licula = pel_licula
        self.preu_entrada = preu_entrada
        self.reserves:list[list[bool]] = [[False] * sala.seients_per_fila for _ in range(sala.files)]
        sala.sessions.append(self)
    
    def mostra_reserves(self) -> None:
        for fila in self.reserves:
            print(fila)

#==========================================================================================================
def obtin_data_hora() -> dt.datetime:
    error = ''
    while True:
        try:
            print(error)
            d = input('Introduïx un data (dd/mm/aa) (intro=Eixir): ')
            data = dt.datetime.strptime(d, '%d-%m-%y')
            h = input('Introduce una hora (hh:mm) (Intro=Eixir): ')
            hora = dt.datetime.strptime(h, "%H:%M").time()
            return dt.datetime.combine(data, hora)
        except ValueError:
            error ='Introducció incorrecta'

#==========================================================================================================
# Manteniment de pel·lícules
#==========================================================================================================
def menu_pel_licules() -> None:
    while True:
        neteja_pantalla()
        print('- LLISTA DE PEL·LÍCULES -')
        if not pel_licules:
            print(' No hi ha pel·licules')
        else:
            for pel_licula in pel_licules:
                print(f'{pel_licula.id} {pel_licula.info}')
        
        opc = input_type('1-Crea, 2-Modifica, 3-Esborra. Opció?')
        if not opc:
            return
        if opc=='1':
            crea_pel_licula()
        elif opc=='2':
            modifica_pel_licula()
        elif opc =='3':
            esborra_pel_licula()
        else:
            print('Opció incorrecta')

#------------------------------------------------------------------------
def crea_pel_licula() -> None:
    print("- CREACIÓ DE PEL·LÍCULES -")
    while True:
        descripcio = input_type('Descripció de la pel·lícula')  
        if not descripcio:
            return
        pel_licula = Pel_licula(descripcio)                     # type: ignore
        pel_licules.append(pel_licula)
        print('Fet')

#------------------------------------------------------------------------
def busca_pel_licula(id: int) -> Pel_licula|None:
    for pel_licula in pel_licules:
            if pel_licula.id==id:
                return pel_licula
    return None

#------------------------------------------------------------------------
def modifica_pel_licula() -> None:
    while True:
        
        if not (id:=input_type('Id de la pel·lícula a modificar','int')):    # type: ignore
            return
                
        if not (pel_licula:=busca_pel_licula(id)):                # type: ignore
            print('Id incorrecte')
            continue
        
        info = input('Nova descripció? ')
        pel_licula.info = info
        print('Fet')

#------------------------------------------------------------------------
def esborra_pel_licula():
    while True:
        if not (id:=input_type('Id de la pel·lícula a esborrar','int')):
            return
        
        if not (pel_licula:=busca_pel_licula(id)):
            print('Id incorrecte')
            continue 

        pel_licules.remove(pel_licula)
        print('Fet')

#------------------------------------------------------------------------
def input_type(text:str, type:str='str') -> int|str|float|None:
    while True:
        try:
            cadena = input(f'(Intro=Eixir) {text} ')
            if cadena=='':
                return None
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
def busca_cine(id: int) -> Cine|None:
    for cine in cines:
        if cine.id==id:
            return cine
    return None            

#------------------------------------------------------------------------
def busca_sala(id: int, cine:Cine) -> Sala|None:
    for sala in cine.sales:
        if sala.id == id:
            return sala
    raise sala_no_trobada

#------------------------------------------------------------------------
def mostra_cine_i_sales() -> None:
    for cine in cines:
        print('---------------------------------')
        print(f'CINE: {cine.id} {cine.descripcio}')
        for sala in cine.sales:
            print(f'   SALA {sala.id} {sala.descripcio}')

#------------------------------------------------------------------------
def selecciona_cine() -> Cine|None:
    if not cines:
        neteja_pantalla()
        error = ' No hi ha cines. Intro per a continuar'
        mostra_titol_i_error('- LLISTA DE CINES -', error )
        input()
        return cine_actiu
    
    neteja_pantalla()
    print('- LLISTA DE CINES -')
    mostra_cine_i_sales()

    while True:
        try: 
            if id_cine:= input_type('Selecciona un cine', 'int'):
                if cine:=busca_cine(id_cine):    # type: ignore
                    return cine
            return None
        except cine_no_trobat:
            print('Cine incorrecte')

#------------------------------------------------------------------------
def mostra_sales_i_sessions(cine:Cine|None) -> None:
    print(f'Cine: {cine_actiu.id} {cine_actiu.descripcio}')                 # type: ignore
    for sala in cine_actiu.sales:
        print('---------------------------------')                                          # type: ignore
        print(f'SALA: {sala.id} {sala.descripcio}')
        if not sala.sessions:
            print('     No hi ha sessions')
            continue
        for sessio in sala.sessions:
            print(f'    SESSIÓ {sessio.id}: {sessio.data_hora.strftime('%d/%m/%y')} {sessio.pel_licula.info}')

#------------------------------------------------------------------------
def demana_sala() -> Sala|None:
    if id_sala:=input_type('Selecciona una sala', 'int'):
        if sala:= busca_sala(id_sala, cine_actiu):
            return sala
    return None
    
#------------------------------------------------------------------------
def mostra_titol_i_error(txt:str, error:str='') -> str:
    print(txt)
    if error:
        print(error)
    return ''

#------------------------------------------------------------------------
def selecciona_sala() -> Sala:  
    neteja_pantalla()
    print('- LLISTA DE SALES I SESSIONS -')
    mostra_sales_i_sessions(cine_actiu)
    while True:
        try:
            if sala:= demana_sala():
                return sala
            return None
        except sala_no_trobada:
            print('Sala incorrecta')

#==========================================================================================================
def mostra_menu() -> None:
    global cine_actiu
    global sala_activa

    while True:
        neteja_pantalla()
        print('- MENÚ PRINCIPAL -')
        print('------------------')
        print('1- Cines i sales')
        print('2- Pel·lícules')
        print('3- Reserves')
        print()
        
        opc = input_type('Opció?')
        if not opc:
            return
        if opc not in ['1','2','3']:
            print('Opció incorrecta')
        elif opc=='1':
            pass                            # Opció no implementada
        elif opc=='2':
            menu_pel_licules()
        elif opc=='3':
            if not cine_actiu:
                cine_actiu = selecciona_cine()
            if cine_actiu:
                sala_activa = selecciona_sala()
        


p1 = Pel_licula('p1')
p2 = Pel_licula('p2')
p3 = Pel_licula('p3')
p4 = Pel_licula('p4')
pel_licules.append(p1)
pel_licules.append(p2)
pel_licules.append(p3)
pel_licules.append(p4)

c1 = Cine('Cine1')
cines.append(c1)

sala1 = Sala(c1, 's1', 3, 4)
sala2 = Sala(c1, 's2', 2, 5)

data1= dt.datetime(2024, 1, 1, 12, 0, 0)
data2= dt.datetime(2024, 1, 1, 14, 0, 0)
data3= dt.datetime(2024, 1, 1, 16, 0, 0)

sessio1 = Sessio(sala1,data1,p1,5)

mostra_menu()
