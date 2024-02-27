from __future__ import annotations

'''En el mateix tren no es pot repetir el mateix vagó'''
class vago_repetit(Exception):
    pass

'''La longitud dels vagons no pot superar la longitud maxima del tren'''
class tren_massa_llarg(Exception):
    pass

class estacions_no_en_ruta(Exception):
    pass

class estacio_final_després_de_la_inicial(Exception):
    '''Una estació final pot ser incorrecta per no existir en la ruta, o
    per estar abans de l'estació inicial.'''
    pass


# ======================================================================================================
class Estacio:
    def __init__(self, nom:str) -> None:
        self.nom = nom
    
    def va_després_de(self, estacio:Estacio, ruta:Ruta) -> bool:
        index1 = ruta.estacions.index(self)
        index2 = ruta.estacions.index(estacio)
        return index2>index1


# ======================================================================================================
class Ruta:
    def __init__(self, nom:str, estacions:list[Estacio]) -> None:
        self.nom = nom
        self.estacions = estacions

    def __eq__(self, obj:object):
        if not isinstance(obj, Ruta):
            return False
        return obj.nom == self.nom


# ======================================================================================================
class Reserva:
    '''No poden hi haver dos reserves iguales, ni en el mateix ni en diferents trens.
       Per a distingir-les tenim l'atribut id, que es forma amb el codi del tren més la data_hora.
       Cada tren té una ruta. La reserva es fa entre una estació inicial i final dins d'esta ruta.
    '''
    def __init__(self, id:str, dni:str, estacio_inicial:Estacio, estacio_final:Estacio) -> None:
        self.id:str = id
        self.dni:str = dni
        self.estacio_inicial:Estacio = estacio_inicial
        self.estacio_final:Estacio = estacio_final

# ======================================================================================================
class Vago:
    '''No poden hi haver dos vagons iguals, ni en el mateix ni en diferents trens. Encara que físicament siga
       el mateix tren amb la mateix matrícula. La raó és que en cada trajecte la llista de reserve associada al vagó
       és diferent'''
    def __init__(self, matricula:str, longitud:int, capacitat: int) -> None:
        self.matricula:str = matricula
        self.longitud:int = longitud
        self.capacitat:int = capacitat
        self.seients: list[list[Reserva]] = [None]*self.capacitat
        # self.reserves:list[Reserva] = []

    # -----------------------------------------------------------------------------
    @property
    def places_lliures(self) -> int:
        return len([s for s in self.seients if s is not None])

    # -----------------------------------------------------------------------------
    @property
    def caben(self, dnis:list[str]) -> bool:
        return self.places_lliures - len(dnis) > self.capacitat

# ======================================================================================================
class Tren:
    '''Cada tren està associat amb un viatge i cada viatge és amb una data_hora diferents. 
       per tant, dos trens no es poden repetir encara que tinguen la mateixa matricula i els mateixos vagons.'''
    longitud_maxima = 300
    def __init__(self, codi:str, ruta:Ruta, data_hora:str) -> None:
        self.codi:str = codi
        self.data_hora = data_hora
        self.ruta:Ruta = ruta
        self.vagons:list[Vago] = []

    # -----------------------------------------------------------------------------
    @property
    def longitud(self):
         return sum(vago.longitud for vago in self.vagons)


    # -----------------------------------------------------------------------------
    def afig(self, vago:Vago) -> None:
        if vago in self.vagons:
            raise vago_repetit
        if self.longitud + vago.longitud > Tren.longitud_maxima:
            raise tren_massa_llarg
        self.vagons.append(vago)

    # -----------------------------------------------------------------------------
    def mostra_reserves(self):
        print('RESERVES')
        for vago in self.vagons:
            print(f'Vago: {vago.matricula}', end='')
            if len(vago.reserves)==0:
                print('. No hi ha reserves.', end='')
            print()
            for reserva in vago.reserves:
                print(f'{reserva.dni=} {reserva.estacio_inicial=} {reserva.estacio_final=}')

    # -----------------------------------------------------------------------------
    def __eq__(self, obj:object) -> True:
        if not isinstance(obj, Tren):
            return False
        return obj.codi==self.codi and obj.data_hora==self.data_hora
    
  
    # -----------------------------------------------------------------------------
    # Primer hem d'omplir vagons. A ser possible, les reserves (quantitat) han d'estar en el mateix vagó.
    def reserva(self, dnis:list[str], estacio_inicial:Estacio, estacio_final:Estacio):
        if not(estacio_inicial in self.ruta.estacions and estacio_final in self.ruta.estacions):
            raise estacions_no_en_ruta
        if estacio_inicial.va_després_de(estacio_final, self.ruta):
            raise estacio_final_després_de_la_inicial
        # Primer busquem quantitat reserves en el mateix vagó, sinó les busquem en vagons diferents.
        for vago in self.vagons:
            if vago.caben([dnis]):
                reserves = [Reserva(self.codi+self.data_hora, dni, estacio_inicial, estacio_final) for dni in dnis]
                vago.reserves.extend(reserves)
                break
        else:


                

# ======================================================================================================
castello = Estacio('Castelló')
benicassim = Estacio('Benicàsim')
orpesa = Estacio('Orpesa')
benicarlo = Estacio('Benicarló')
vinaros = Estacio('Vinarós')

ruta_castello_vinaros = Ruta('Castelló-Vinarós',[castello,benicassim,orpesa,benicarlo,vinaros])

vago1 = Vago(matricula='VAGO_001', longitud=50, capacitat=100)
vago2 = Vago(matricula='VAGO_002', longitud=60, capacitat=120)
vago3 = Vago(matricula='VAGO_003', longitud=40, capacitat=80)

tren1 = Tren(codi='TALGO_001', ruta=ruta_castello_vinaros, data_hora='01/01/2024 10:00')
tren1.afig(vago1)
tren1.afig(vago2)
tren1.afig(vago3)


tren1.mostra_reserves()
