import csv
import json


def write_to_file(data):
    with open('files/data.json', 'w') as f:        # otworz plik, wykonaj ponizszy kod i zamknij plik
        json.dump(data, f)                         # data - dane, f - file (zapisuje x do pliku)


def read_from_file():
    with open('files/data.json', 'r') as f:
        data = json.load(f)                     # f - file (odczytuje z pliku do zmiennej)
        return data


class Student:
    def __init__(self, imie, nazwisko):
        self.student = {
            'imie' : imie,
            'nazwisko': nazwisko
        }


    def add_student(self):
        data['students'].append(self.student)


# data = {
#     'students' : []
# }

# with open('files/data.json', 'w') as f:     # stworz plik data.json
#     pass
#
# student1 = Student('Bartosz', 'Bizański')
# student2 = Student('Michał', 'Kaczmarek')
# student3 = Student('Ludi', 'Pilch')
# student4 = Student('Julcia', 'Mika')
# student1.add_student()
# student2.add_student()
# student3.add_student()
# student4.add_student()
#
# write_to_file(data)


def search_for_name(name):
    found = None
    for i in data['students']:
        if i['imie'] == name:
            found = True
            return i
    if not found:
        return False


def add_new_student():
    name = input('Podaj imię: ')
    surname = input('Podaj nazwisko: ')
    new_student = Student(name, surname)
    new_student.add_student()
    # write_to_file(data)
    print(f'Dodano {name} {surname}')


def print_all():
    for i in data['students']:
        print(f"{i['imie']} {i['nazwisko']}")


def search():
    name = input('Podaj imie: ')
    found = search_for_name(name)
    if not found:
        print(f'Nie znaleziono {name}')
    else:
        print(f"{found['imie']} {found['nazwisko']}")


def delete():
    name = input('Podaj imie: ')
    found = search_for_name(name)
    if not found:
        print(f'Nie znaleziono {name}')
    else:
        if 'y' == input(f"Czy na pewno usunąć {found['imie']} {found['nazwisko']}? Nie będzie można cofnąć tego działania (y/n)").lower():
            data['students'].remove(found)
            print(f"Usunięto {found['imie']} {found['nazwisko']} z listy studentów")
        else:
            print(f"Nie usunięto.")


def exporter(data):
    with open('files/data.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['imie', 'nazwisko'])
        writer.writeheader()
        writer.writerows(data['students'])


def export_csv():
    # raise NotImplementedError('This functionality is not implemented yet :c')
    want = input('Czy na pewno chcesz wyeksportować dane do pliku CSV? (y/n) ').lower()
    if want == 'y':
        exporter(data)
        print('Wyeksportowano dane studentów do pliku data.csv')
    else:
        print('Nie wyeksportowano')


    # ---------------------------------------------------------------------------------------------------------------
menu = {
    'l': print_all,
    'a': add_new_student,
    's': search,
    'd': delete,
    'e': export_csv,
}

data = read_from_file()     # start programu, wczytanie danych z pliku

print('Witamy w programie lista sudentów')
while True:
    inp = input("""Co chcesz zrobić?
    l - wypisz listę wszystkich studentów
    a - dodaj nowego studenta 
    s - szukaj studenta
    d - usuń studenta
    e - eksportuj listę do formatu csv
    q - wyjście
    """)
    inp.lower()

    if inp in menu:
        try:
            menu[inp]()
        except NotImplementedError:
            print('Przepraszamy, ta funkcjonalność nie jest jeszcze dostępna')
    elif inp == 'q':
        break
    else:
        print(f"Nie znaleziono polecenia {inp}, spróbuj ponownie")

write_to_file(data)         # koniec programu, zapis danych do pliku
print('Dziękujemy za skorzystanie i życzymy smacznej kawusi UwU')
# ---------------------------------------------------------------------------------------------------------------


'''
POLECENIE:
l - wypisz listę wszystkich studentów DONE
q - wyjście DONE
a - dodaj nowego studenta DONE
s - szukaj studenta DONE
d - usuń studenta DONE
e - eksportuj listę do formatu csv DONE
'''

