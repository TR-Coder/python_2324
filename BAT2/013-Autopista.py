# Enunciat
# Una Persona s'identifica pel seu dni
# Un Cotxe s'identifica per una matrícula i una capacitat d'ocupants (per defecte 4) i per una llista dels seus ocupants (persones)
#   Mètodes:
#       - def entra(self, persona). Error si la persona ja està en el cotxe i se supera la capacitat del Cotxe.
#       - def ix(self, persona). Error si la persona no està en el cotxe.
#       - Mètode per a mostrar els dni dels ocupants del cotxe.
# Una Autopista queda definida per una llista dels cotxes que circulen per ella.
#   Mètodes:
#       - def entra(self, cotxe).
#       - def ix(self, cotxe). Error si intenta traure un cotxe que no està en la autopista.
#       - Mètode per a mostrar la matrícula dels cotxes que estan en l'autopista.

# -----------------------------------------------------------------------------------
class Cotxe_no_en_autopista(Exception):
    pass

class Cotxe_ple(Exception):
    pass

class Persona_ja_està_en_cotxe(Exception):
    pass

class Persona_no_este_cotxe(Exception):
    pass
# -----------------------------------------------------------------------------------

class Autopista:
    def __init__(self):
        self.vehicles = []
    def entra(self, cotxe):
        self.vehicles.append(cotxe)
    def ix(self, cotxe):
        try:
            self.vehicles.remove(cotxe)
        except ValueError:
            raise Cotxe_no_en_autopista
    def __str__(self):
        matricula_cotxes = [str(vehicle.matricula) for vehicle in self.vehicles]
        return ' '.join(matricula_cotxes)

#==================================================================================
class Persona:
    def __init__(self, dni):
        self.dni = dni

    def _eq_(self, persona):
        return self.dni == persona.dni
    

#==================================================================================
class Cotxe:
    def __init__(self, matricula, capacitat=4):
        self.matricula = matricula
        self.ocupants = []
        self.capacitat = capacitat

    
    def entra(self, persona):
        if len(self.ocupants)>self.capacitat:
            raise Cotxe_ple
        if persona in self.ocupants:
            raise Persona_ja_està_en_cotxe
        self.ocupants.append(persona)

    def ix(self, persona):
        try:
            self.ocupants.remove(persona)
        except ValueError:
            raise Persona_no_este_cotxe

    def ix2(self, persona):
        self.ocupants = [ocupant for ocupant in self.ocupants if ocupant.dni==persona.dni]

    def __eq__(self, cotxe):
        return self.matricula == cotxe.matricula

    def __str__(self):    
        dni_ocupants = [str(ocupant.dni) for ocupant in self.ocupants]
        return ' '.join(dni_ocupants)
    

#==================================================================================

p1 = Persona(111)
p2 = Persona(222)
p3 = Persona(9999)

c1 = Cotxe('2341DFF')
c2 = Cotxe('21354FW')

c1.entra(p1)
c1.entra(p1)
print(c1)

# a7 = Autopista()
# a7.entra(c1)
# print(a7)