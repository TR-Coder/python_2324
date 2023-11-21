# https://www.geeksforgeeks.org/python-match-case-statement/

#
# Com la sentència case.
# A més tenim l'operador | (pipe)
#
command = 'Hello'
match command:
    case 'Hello, World!' | 'Hello':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later')
    case other:
        print('No match found')


#
# afegir al case una setència if
# _ is a wildcard pattern that matches any value of n not already matched by previous patterns.
#
def runMatch():
    user = str(input("Write your username -: "))
    allowedDataBaseUsers = ["Rishabh"]
    match user:
        case "Rishabh" if user in allowedDataBaseUsers:
            print("You are allowed to access the database !")
        case _:
            print("you are not  allowed to access the code !")
    
#
# patrons
#

def file_handler_v1(command):
    match command.split():
        case ['show']:
            print('List all files and directories: ')
        case ['remove', *files]:
            print(f'Removing files: {files}')
        case _:
            print('Command not recognized')

file_handler_v1('remove file1.txt file2.jpg file3.pdf')



def file_handler_v2(command):
    match command.split():
        case ['show']:
            print('List all files and directories: ')
        case ['remove' | 'delete', *files] if '--ask' in files:
            del_files = [f for f in files if len(f.split('.'))>1]
            print('Please confirm: Removing files: {}'.format(del_files))
        case ['remove' | 'delete', *files]:
            print('Removing files: {}'.format(files))
        case _:
            print('Command not recognized')

file_handler_v2('remove --ask file1.txt file2.jpg file3.pdf')



def runMatch2(data_input):
    match data_input:
        case ["a"]:
            print("The list only contains a and is just a single list")
 
        case ["a", *other_items]:
            print(f"The 'a' is the first element and {other_items} are the rest  of the elements !")
 
        case [*first_items, "d"] | (*first_items, "d"):
            print(f"The 'd' is the last item and {first_items} are the previous elements before it !")
        case  _:
            print("No case matches with this one !")
 
 
runMatch2(["a"])
runMatch2(("a", "b"))
runMatch2(["a", "b", "c", "d"])
runMatch2(["b", "c", "d"])


punts = [(0,2), (3,0), (4,5)]
for p in punts:
    match p:
        case (0,y):
            print('Punt sobre Y')
        case (x,0):
            print('Punt sobre x')   
        case _:
            print('No està sobre cap eix')



#
# classes
#
# El case no crea cap instància de la classe.
# Verifica que el objecte és de la classe indicada i que els atributs tenen els valors indicats.


from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int
	salary: int


@dataclass
class Programmer:
	name: str
	language: str
	framework: str

def runMatch3(instance):
	match instance:
		case Programmer("Om", language="Python", framework="Django"):
			print("He is Om and he is a Python programmer and uses Django Framework!")
		case Programmer("Rishabh", "C++"):
			print("He is Rishabh and is a C++ programmer !")
		case Person("Vishal", age=5, salary=100):
			print("He is vishal and he is a kid !")
		case Programmer(name, language, framework):
			print(f"He is programmer , his name is {name} he works in {language} and uses {framework} !")
		case Person():
			print("He is just a person !")
		case _:
			print("This person is nothiing !")

programmer1 = Programmer("Om", "Python", "Django")
programmer2 = Programmer("Rishabh", "C++", None)
programmer3 = Programmer("Sankalp", "Javascript", "React")
person1 = Person("Vishal", 5, 100)
runMatch3(programmer1)
runMatch3(programmer2)
runMatch3(person1)
runMatch3(programmer3)


#
# diccionaris
# Podem fer que case la clau i el valor, o només la clau amb qualsevol valor.
#


def runMatch4(dictionary):
    match dictionary:
        case {"name": "Om"}:
            print("This matches only for one key, that is if they key exists with  the pair value then this block will be selected !")
        case {"framework": "Django", "language": "Python"}:
            print("This one matches multiple keys and values . !")
        case {"name": namex, "language": languagey, "framework": frameworkz}:
            print(f"The person's name is {namex}, the language he uses is {languagey} and the framework he uses is {frameworkz} !")
        case _:
            print("Matches anything !")
a = {
     "name": "Om",
     "language": "Python",
     "framework": "Django",
    }

runMatch4(a)
a["name"] = "Rishabh"
runMatch4(a)
a["language"] = "C++"
runMatch4(a)


# https://blog.enterprisedna.co/python-match-case/