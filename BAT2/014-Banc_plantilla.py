from enum import Enum

LINE_UP = '\033[1F'
LINE_CLEAR = '\x1b[2K'

# ===========================================================================
# Tipus_Moviment
# ===========================================================================
class Tipus_Moviment(Enum):
    INGRES = 0
    REINTEGRAMENT = 1
    TRANSFERENCIA_ENTRADA = 2
    TRANSFERENCIA_EIXIDA = 3

# ===========================================================================
# classes d'error
# ===========================================================================
class Error(Exception):
    def __init__(self, missatge: str, *args):
        self.missatge = missatge

class Tipus_moviment_incorrecte(Exception):
    pass

class Moviment_quantitat_negativa(Exception):
    pass

class No_hi_ha_compte_actiu(Exception):
    pass

class Saldo_inicial_negatiu(Exception):
    pass

class IBAN_incorrecte(Exception):
    pass

class Transferencia_supera_saldo(Exception):
    pass

class Reintegrament_supera_saldo(Exception):
    pass

# ===========================================================================
# Compte
# ===========================================================================
# 'No es pot crear un compte amb saldo inicial negatiu'
# 'Un compte ha de tindre sempre un IBAN'
class Compte:
    def __init__(self, nom_titular: str, iban: str, saldo_inicial: float = 0):
        # Inicialització atributs
        self.moviments: list[Moviment] = []
        self.saldo:float = 0
        # Generar moviment Ingres amb saldo_inicial
        pass

    # ------------------------------------------------------------------------
    def ingressa(self, quantitat: float):
        # Generar moviment Ingres amb quantitat
        pass

    # ------------------------------------------------------------------------
    # 'Intents de traure més quantitat que el saldo disponible'
    def reintegrament(self, quantitat: float):
        # Generar moviment Reintegrament amb quantitat
        pass

    # ------------------------------------------------------------------------
    def mostra_saldo(self):
       pass

    # ------------------------------------------------------------------------
    def mostra_llista_moviments(self):
        # Mostra llista moviments i el saldo actual
        pass
 
    # 'Intents de transferir més quantitat que el saldo disponible'
    def transferix(self, compte: Compte, quantitat: float):
        # Generar moviment eixida i entrada amb quantitat
        pass

    # ------------------------------------------------------------------------
    def _moviment(self, tipus: Tipus_Moviment, quantitat: float):
        moviment = Moviment(tipus, quantitat)
        self.moviments.append(moviment)
        if (tipus == Tipus_Moviment.INGRES) or (tipus == Tipus_Moviment.TRANSFERENCIA_ENTRADA):
            self.saldo += quantitat
        elif (tipus == Tipus_Moviment.REINTEGRAMENT) or (tipus == Tipus_Moviment.TRANSFERENCIA_EIXIDA):
            self.saldo -= quantitat

# ===========================================================================
# Moviment
# ===========================================================================
# 'Intent de crear un moviment amb quantitat negativa'
class Moviment:
    def __init__(self, tipus_moviment: Tipus_Moviment, quantitat: float, compte_destinacio: Compte = None):
        # Inicialització atributs
        pass

# ===========================================================================
# Banc
# ===========================================================================
class Banc:
    msg_no_hi_ha_compte_actiu: str = 'Error, no hi ha cap compte actiu'

    # ------------------------------------------------------------------------
    def __init__(self):
        self.compte_actiu: Compte = None
        self.comptes: list[Compte] = []

    # ------------------------------------------------------------------------
    def mostra_compte_actiu(self):
        pass
 
    # ------------------------------------------------------------------------
    def _hi_ha_compte_actiu(self) -> bool:
        return bool(self.compte_actiu)

    # ------------------------------------------------------------------------
    def _mostra_titol(self, titol: str):
        print(f'- {titol} -'.upper())
        if not self._hi_ha_compte_actiu():
            raise No_hi_ha_compte_actiu('No hi ha compte actiu')

    # ------------------------------------------------------------------------
    # Recorre la llista de comptes i verifiquen si ja existix un compte amb nom i iban que li passem
    def _compte_ja_existix(self, nom: str, iban: str) -> bool:
        pass

    # ------------------------------------------------------------------------
    def _mostra_missatge_error(self, text:str):
        print('' if text=='' else f'ERROR: {text}\n')

    # ------------------------------------------------------------------------
    # Crea un compte i l'afegix a la llista de comptes del banc.
    # Demana la informació a l'usuari
    def crea_compte(self):
        msg_error: str = ''
        print('- CREACIÓ DE COMPTES BANCARIS -')

        while True:
            try:

                pass

            except ValueError:
                msg_error = 'Saldo inicial incorrecte'
            except Saldo_inicial_negatiu:
                msg_error = 'El saldo no pot ser negatiu'
            except IBAN_incorrecte:
                msg_error = 'IBAN incorrecte'
            else:
                msg_error = ''

        if not self._hi_ha_compte_actiu():
            self.compte_actiu = compte

    # ------------------------------------------------------------------------
    # Demana a l'usuari un iban i posa com actiu el corresponent compte.
    def selecciona_compte_actiu(self):
        print('- CANVIA COMPTE ACTIU -\n')
        pass

    # ------------------------------------------------------------------------
    # Busca un compte amb iban o nom_titular
    def _busca_compte(self, iban: str = '', nom_titular: str = '') -> Compte | None:
        pass

    # ------------------------------------------------------------------------
    def mostra_saldo(self):
        self._mostra_titol('Mostra saldo')
        self.compte_actiu.mostra_saldo()
        input('\nIntro per a continuar ')

    # ------------------------------------------------------------------------
    # Demana a l'usuari una quantitat a ingressar.
    # Fa l'ingrés en el compte actiu
    def ingressa_diners(self):
        msg_error: str = ''
        self._mostra_titol('Ingressos')

        while True:
            try:

                pass

            except ValueError:
                msg_error = 'Quantitat incorrecta'
            except Moviment_quantitat_negativa:
                msg_error = 'La quantitat a ingressar ha de ser positiva'
            else:
                msg_error = ''

    # ------------------------------------------------------------------------
    # Demana a l'usuari una quantitat a traure.
    # Fa el reintegrament en el compte actiu
    def reintegrament(self):
        msg_error: str = ''
        self._mostra_titol('Reintegrament')

        while True:
            try:

                pass

            except ValueError:
                msg_error = 'Quantitat incorrecta'
            except Moviment_quantitat_negativa:
                msg_error = 'La quantitat de reintegrament ha de ser positiva'
            except Reintegrament_supera_saldo as e:
                saldo_disponible = e.args[1]
                msg_error = f'La quantitat a traure supera el saldo disponible de {saldo_disponible}'
            else:
                msg_error = ''

    # ------------------------------------------------------------------------
    # Demana a l'usuari un compte i una quantitat a què transferir.
    # Fa la transferència en el compte_actiu
    def tranferencia(self):
        msg_error: str = ''
        self._mostra_titol('Transferencia')

        while True:
            try:

                pass
            
            except ValueError:
                msg_error = 'Quantitat incorrecta'
            except Moviment_quantitat_negativa:
                msg_error = 'La quantitat no pot ser negativa'
            except Transferencia_supera_saldo as e:
                saldo_disponible = e.args[1]
                msg_error = f'La quantitat a transferir supera el saldo disponible de {saldo_disponible}'
            else:
                msg_error = ''


    # ------------------------------------------------------------------------
    def consulta_moviments(self):
        self._mostra_titol('Consulta de moviments')
        self.compte_actiu.mostra_llista_moviments()
        input('\nIntro per a continuar ')

    # ------------------------------------------------------------------------
    def consulta_comptes(self):
        print('- CONSULTA DE COMPTES -')
        for compte in self.comptes:
            print(f'\nNom: {compte.nom_titular}')
            print(f'IBAN: {compte.iban}')
            print(f'Saldo: {compte.saldo}')
        input('\nIntro per a continuar ')

# ===========================================================================
# Programa principal
# ===========================================================================
from typing import Callable
import os
import platform

banc = Banc()

opcions_menu: list[str] = [
	'1- Selecciona el compte actiu',
	'2- Ingrés de diners',
	'3- Reintegrament de diners',
	'4- Transferència entre comptes',
	'5- Consulta de moviments',
	'6- Mostra el saldo actual',
	'7- Crea un nou compte bancari',
	'8- Consulta tots els comptes',
	'9- Acaba el programa'
]

executa_metode: dict[str,Callable] = {
    '1': banc.selecciona_compte_actiu,
    '2': banc.ingressa_diners,
    '3': banc.reintegrament,
    '4': banc.tranferencia,
    '5': banc.consulta_moviments,
    '6': banc.mostra_saldo,
    '7': banc.crea_compte,
    '8': banc.consulta_comptes,
    '9': exit,
}      

# ------------------------------------------------------------------------
def neteja_pantalla():
    # """Neteja la terminal (cls o clear). Té en compte els sistema operatiu (Windows,Linux)"""
    comando = 'cls' if platform.system()=='Windows' else 'clear'
    os.system(comando)

# ------------------------------------------------------------------------
def mostra_opcions_menu():
    for opcio in opcions_menu:
        print(opcio)
    print()

# ------------------------------------------------------------------------
def mostra_menu_principal():
    neteja_pantalla()
    print('   -- MENÚ PRINCIPAL --')
    mostra_opcions_menu()

# ------------------------------------------------------------------------
def entrada_teclat(text:str, tipus:str = 'str') -> str|int|float:
    entrada = input(text + ' ')
    if tipus == 'str':
        return entrada
    elif tipus == 'int':
        return int(entrada)
    elif tipus == 'float':
        return float(entrada)

    raise Exception('tipus entrada_teclat no definida')

# ------------------------------------------------------------------------
def entrada_opcio (msg_error:str) -> str:
    if msg_error == '':
        return input('\nOpció: ')
    else:
        text = '' if msg_error=='' else f'ERROR: {msg_error}'
        print('\n\n'+ text, end='')
        opcio = input(LINE_UP + 'Opció: ')
        print() 
        return opcio

# ------------------------------------------------------------------------
msg_error = ''

while True:
    try:
        mostra_menu_principal()
        banc.mostra_compte_actiu()
        opcio = entrada_opcio(msg_error)
        print()
        executa_metode[opcio]()
    except KeyError:
        msg_error = "Error: opció incorrecta"
    except No_hi_ha_compte_actiu:
        msg_error = 'Error: No hi ha compte actiu'
    else:
        msg_error = ''
