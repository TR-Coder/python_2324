# --------------------------------------------------------------------------------------------
# Manteniment d'un diccionari.
# --------------------------------------------------------------------------------------------

qualificacions:dict = {}

while True:
    print()
    print(qualificacions)
    print('    MENU')
    print('-------------')
    print('A- afegir')
    print('E- esborrar')
    print('M- modificar nota')
    print('C- modificar nom assignatura')
    print('Q- Acabar')

    opcio = input('Opció? ').upper()

    if opcio == 'Q':
        break

    elif opcio == '':
        pass

    elif opcio == 'A':
        print('Acabar la introducció amb <intro>')
        while True:
            nom = input('Nom assignatura: ').strip().title()

            if nom == '':
                break

            if nom in qualificacions:
                print("Error, l'assignatura ja existix")
                continue

            nota = float(input('Nota: '))
            qualificacions[nom] = nota

    elif opcio == 'E':
        nom = input("Esborrar l'assignatura: ").strip().title()
        try:
            qualificacions.pop(nom)
        except KeyError:
            print("Error, l'asignatura no està creada")

    elif opcio == 'M':
        nom = input('Nom assignatura a modificar? ').strip().title()
        if nom not in qualificacions:
            print("Error, l'assignatura no existix")
            continue

        nota = float(input('Nota: '))
        qualificacions[nom] = nota

    elif opcio == 'C':
        nom_antic = input('Nom assignatura a canviar? ').strip().title()
        if nom_antic not in qualificacions:
            print("Error, l'assignatura no existix")
            continue

        nom_nou = input('Nom nou assignatura: ').strip().title()
        if nom_nou in qualificacions:
            print("Error, l'assignatura ja existix")
            continue

        valor = qualificacions.pop(nom_antic)
        qualificacions[nom_nou] = valor

    else:
        print('Error: opció incorrecta\n')
