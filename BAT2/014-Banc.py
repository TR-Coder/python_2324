from __future__ import annotations
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
class Compte:
    def __init__(self, nom_titular: str, iban: str, saldo_inicial: float = 0):
        if saldo_inicial < 0:
            raise Saldo_inicial_negatiu('No es pot crear un compte amb saldo inicial negatiu')
        if iban == '':
            raise IBAN_incorrecte('Un compte ha de tindre sempre un IBAN')
        self.nom_titular: str = nom_titular
        self.iban: str = iban
        self.moviments: list[Moviment] = []
        self.saldo:float = 0
        self._moviment(Tipus_Moviment.INGRES, saldo_inicial)   

    # ------------------------------------------------------------------------
    def ingressa(self, quantitat: float):
        self._moviment(Tipus_Moviment.INGRES, quantitat)

    # ------------------------------------------------------------------------
    def reintegrament(self, quantitat: float):
        if quantitat > self.saldo:
            raise Reintegrament_supera_saldo('Intents de traure més quantitat que el saldo disponible', self.saldo)
        self._moviment(Tipus_Moviment.REINTEGRAMENT, quantitat)

    # ------------------------------------------------------------------------
    def mostra_saldo(self):
        print(f'El saldo de {self.nom_titular} és {self.saldo}')

    # ------------------------------------------------------------------------
    def mostra_llista_moviments(self):
        for moviment in self.moviments:
            print(f'> {moviment.tipus_moviment} {moviment.quantitat} ', end='')
            if moviment.compte_destinacio:
                print(f'Compte destinacio: {moviment.compte_destinacio.iban}', end='')
            print()
        print(f'Saldo: {self.saldo}\n')
 
    # ------------------------------------------------------------------------
    # PUFF: no és una transacció !!
    # ------------------------------------------------------------------------
    def transferix(self, compte: Compte, quantitat: float):
        if quantitat > self.saldo:
            raise Transferencia_supera_saldo('Intents de transferir més quantitat que el saldo disponible', self.saldo)
        self._moviment(Tipus_Moviment.TRANSFERENCIA_EIXIDA, quantitat)
        compte._moviment(Tipus_Moviment.TRANSFERENCIA_ENTRADA, quantitat)

    # ------------------------------------------------------------------------
    def _moviment(self, tipus: Tipus_Moviment, quantitat: float):
        # IMPORTANT crear primer el Moviment() i després modificar el saldo ja que Moviment pot llançar una excepció. Si modificarem 
        # primer el saldo i després ferem Moviment, si Moviment fallara el saldo es quedaria malament.
        moviment = Moviment(tipus, quantitat)
        self.moviments.append(moviment)
        if (tipus == Tipus_Moviment.INGRES) or (tipus == Tipus_Moviment.TRANSFERENCIA_ENTRADA):
            self.saldo += quantitat
        elif (tipus == Tipus_Moviment.REINTEGRAMENT) or (tipus == Tipus_Moviment.TRANSFERENCIA_EIXIDA):
            self.saldo -= quantitat

# ===========================================================================
# Moviment
# ===========================================================================
class Moviment:
    def __init__(self, tipus_moviment: Tipus_Moviment, quantitat: float, compte_destinacio: Compte|None = None):
        self.tipus_moviment = tipus_moviment
        self.quantitat = quantitat
        self.compte_destinacio = compte_destinacio
        if quantitat < 0:
            raise Moviment_quantitat_negativa('Intent de crear un moviment amb quantitat negativa')

# ===========================================================================
# Banc
# ===========================================================================
class Banc:
    msg_no_hi_ha_compte_actiu: str = 'Error, no hi ha cap compte actiu'

    # ------------------------------------------------------------------------
    def __init__(self) -> None:
        self.compte_actiu: Compte|None = None
        self.comptes: list[Compte] = []

    # ------------------------------------------------------------------------
    def mostra_compte_actiu(self):
        if self._hi_ha_compte_actiu():
            print(f'Compte actiu: {self.compte_actiu.iban}, {self.compte_actiu.nom_titular}')
        else:
            print('No hi ha compte actiu')
 
    # ------------------------------------------------------------------------
    def _hi_ha_compte_actiu(self) -> bool:
        return bool(self.compte_actiu)

    # ------------------------------------------------------------------------
    def _mostra_titol(self, titol: str):
        print(f'- {titol} -'.upper())
        if not self._hi_ha_compte_actiu():
            raise No_hi_ha_compte_actiu('No hi ha compte actiu')

    # ------------------------------------------------------------------------
    def _compte_ja_existix(self, nom: str, iban: str) -> bool:
        for compte in self.comptes:
            if compte.iban == iban or compte.nom_titular == nom:
                return True
        return False

    # ------------------------------------------------------------------------
    def _mostra_missatge_error(self, text:str):
        print('' if text=='' else f'ERROR: {text}\n')

    # ------------------------------------------------------------------------
    def crea_compte(self) -> None:
        msg_error: str = ''
        print('- CREACIÓ DE COMPTES BANCARIS -')

        while True:
            try:
                self._mostra_missatge_error(msg_error)
                nom:str = entrada_teclat('Nom del titular (intro=eixir):')  # type: ignore
                if nom == '':
                    return
                iban:str = entrada_teclat('IBAN:')  # type: ignore
                saldo: float = entrada_teclat('Saldo inicial:', tipus='float')  # type: ignore
                if self._compte_ja_existix(nom, iban):
                    msg_error = 'Ja existix un compte amb el mateix nom de titular o IBAN'
                    continue
                compte = Compte(nom, iban, saldo)
                self.comptes.append(compte)
                print('OK')
            except ValueError:
                msg_error = 'Saldo inicial incorrecte'
            except Saldo_inicial_negatiu:
                msg_error = 'El saldo no pot ser negatiu'
            except IBAN_incorrecte:
                msg_error = 'IBAN incorrecte'
            else:
                msg_error = ''

    # ------------------------------------------------------------------------
    def selecciona_compte_actiu(self) -> None:
        print('- CANVIA COMPTE ACTIU -\n')
        while True:
            iban:str = entrada_teclat('IBAN del compte (intro eixir):') # type: ignore
            if iban == '':
                return
            compte: Compte = self._busca_compte(iban=iban)  # type: ignore
            if compte:
                self.compte_actiu = compte
                return

            print("No s'ha trobat el compte\n")

    # ------------------------------------------------------------------------
    def _busca_compte(self, iban: str = '', nom_titular: str = '') -> Compte | None:
        for compte in self.comptes:
            if compte.iban == iban or compte.nom_titular == nom_titular:
                return compte
        return None

    # ------------------------------------------------------------------------
    def mostra_saldo(self):
        self._mostra_titol('Mostra saldo')
        self.compte_actiu.mostra_saldo()
        input('\nIntro per a continuar ')

    # ------------------------------------------------------------------------
    def ingressa_diners(self) -> None:
        msg_error: str = ''
        self._mostra_titol('Ingressos')

        while True:
            try:
                self._mostra_missatge_error(msg_error)
                quantitat: float = entrada_teclat('Quantitat a ingressar (0=eixir):', tipus='float')    # type: ignore
                if quantitat == 0:
                    return
                self.compte_actiu.ingressa(quantitat)   # type: ignore
                return
            except ValueError:
                msg_error = 'Quantitat incorrecta'
            except Moviment_quantitat_negativa:
                msg_error = 'La quantitat a ingressar ha de ser positiva'
    

    # ------------------------------------------------------------------------
    def reintegrament(self) -> None:
        msg_error: str = ''
        self._mostra_titol('Reintegrament')

        while True:
            try:
                self._mostra_missatge_error(msg_error)
                quantitat: float = entrada_teclat('Quantitat a traure: (0=eixir)', tipus='float')   # type: ignore
                if quantitat == 0:
                    return
                self.compte_actiu.reintegrament(quantitat)  # type: ignore
                return
            except ValueError:
                msg_error = 'Quantitat incorrecta'
            except Moviment_quantitat_negativa:
                msg_error = 'La quantitat de reintegrament ha de ser positiva'
            except Reintegrament_supera_saldo as e:
                saldo_disponible = e.args[1]
                msg_error = f'La quantitat a traure supera el saldo disponible de {saldo_disponible}'
            
    # ------------------------------------------------------------------------
    def tranferencia(self) -> None:
        msg_error: str = ''
        self._mostra_titol('Transferencia')

        while True:
            try:
                self._mostra_missatge_error(msg_error)
                iban:str = entrada_teclat('IBAN del compte a què volem tranferir diners (intro=eixir):')    # type: ignore
                if iban == '':
                    return
                compte_destinacio = self._busca_compte(iban=iban)
                if not compte_destinacio and compte_destinacio not in self.comptes:
                    msg_error = 'El compte no existix'
                    continue
                if compte_destinacio == self.compte_actiu:
                    msg_error = 'No es pot fer una transferència sobre el mateix compte'
                    continue
                quantitat: float = entrada_teclat('Quantitat de diners a transferir:', tipus='float')   # type: ignore
                self.compte_actiu.transferix(compte_destinacio, quantitat)  # type: ignore
                return
            except ValueError:
                msg_error = 'Quantitat incorrecta'
            except Moviment_quantitat_negativa:
                msg_error = 'La quantitat no pot ser negativa'
            except Transferencia_supera_saldo as e:
                saldo_disponible = e.args[1]
                msg_error = f'La quantitat a transferir supera el saldo disponible de {saldo_disponible}'

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
