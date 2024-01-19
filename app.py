import sqlite3
import pandas as pd

conn = sqlite3.connect('tasks.db')
cursor=conn.cursor()
cursor.execute('''
                   CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   description TEXT,
                   category TEXT,
                   completed BOOLEAN DEFAULT 0
                   )
                   ''')
conn.commit()


def unos_zadatka():
    name = input("Unesite naziv zadatka: ")
    description = input("Unesite opcionalni opis zadatka: ")
    
    while True:
        category = input("Unesite kategoriju zadatka (Dnevni, Tjedni, Mjesečni, Godišnji): ")
        valid_categories = ['Dnevni', 'Tjedni', 'Mjesečni', 'Godišnji']
        
        if category in valid_categories:
            break
        else:
            print("Neispravan unos kategorije. Molimo odaberite između Dnevnog, Tjednog, Mjesečnog ili Godišnjeg.")

    conn.execute('''
                 INSERT INTO tasks (name, description, category, completed)
                 VALUES (?, ?, ?, ?)
                 ''', (name, description, category, 0))
    conn.commit()


def ispis_zadataka():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    df = pd.DataFrame(tasks, columns=["ID", "Naziv", "Opis", "Kategorija", "Dovršen"])
    
    print(df)

    if not tasks:
        print("Nema unesenih zadataka. ")    


def brisanje_zadatka():
    while True:
        print("\nUnesite 1 za brisanje pojedinačnog zadatka")
        print("Unesite 2 za brisanje svih zadataka određene kategorije")
        print("Unesite 3 za brisanje svih zadataka svih kategorija")
        izbor = int(input("Unesite odabir za brisanje zadataka: "))

        if izbor == 1:
            id = int(input("Unesite ID zadatka koji želite obrisati: "))
            # Provjera postojanja zadatka prije brisanja
            cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,))
            existing_task = cursor.fetchone()
            if existing_task:
                cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
                print(f"Zadatak (ID: {id}) je uspješno izbrisan.")
                conn.commit()
            else:
                print(f"Zadatak s ID-om {id} ne postoji. Nema zadatka za brisanje.")

            break

        elif izbor == 2:
            kategorija = input("Unesite kategoriju zadataka koje želite izbrisati: ")
            # Provjera postojanja zadataka prije brisanja
            cursor.execute('SELECT * FROM tasks WHERE category = ?', (kategorija,))
            existing_tasks = cursor.fetchall()
            if existing_tasks:
                cursor.execute('DELETE FROM tasks WHERE category = ?', (kategorija,))
                conn.commit()
                print(f"Svi zadaci iz kategorije '{kategorija}' su uspješno obrisani.")
            else:
                print(f"Nema zadataka u kategoriji '{kategorija}'. Nema zadatka za brisanje.")

            break

        elif izbor == 3:
            # Provjera postojanja bilo kojeg zadatka prije brisanja svih zadataka
            cursor.execute('SELECT * FROM tasks')
            existing_tasks_all = cursor.fetchall()
            if existing_tasks_all:
                cursor.execute('DELETE FROM tasks')
                conn.commit()
                print("Svi zadaci su uspješno obrisani.")
            else:
                print("Nema zadataka. Nema zadatka za brisanje.")

            break

        else:
            print("Nevažeči odabir, molimo pokušajte ponovno.")
            

def oznacavanje_dovrsenim():
    id=int(input("Unesite ID zadatka koji želite označiti dovršenim: "))
    cursor.execute('UPDATE tasks SET completed=1 WHERE id = ?', (id,))

   
def ispis_grupa_zadataka():
    while (True):
        kategorija=input("Unesite kategoriju za prikaz zadataka: ")
        cursor.execute('SELECT * FROM tasks WHERE category = ?', (kategorija,))
        zadaci=cursor.fetchall()

        if zadaci:
          print(f"Zadaci iz kategorije '{kategorija}':")
          df = pd.DataFrame(zadaci, columns=["ID", "Naziv", "Opis", "Kategorija", "Dovršen"])
          print(f"Zadaci iz kategorije '{kategorija}':")
          print(df)
          break
        else:
          print(f"Nema zadataka u kategoriji '{kategorija}'.")



def main():
    while True:
        print("---------------------------------------------")
        print("\nOdaberite opciju:")
        print("1. Dodaj zadatak: ")
        print("2. Označi zadatak dovršenim")
        print("3. Brisanje zadataka")
        print("4. Ispis svih zadataka")
        print("5. Ispis svih zadataka određene kategorije")
        print("0. Izlazak iz programa")
        print("---------------------------------------------")

        izbor=int(input("Unesite izbor:"))

        if izbor==1:
            unos_zadatka()
        elif izbor==2:
            oznacavanje_dovrsenim()
        elif izbor==3:
            brisanje_zadatka()
        elif izbor==4:
            ispis_zadataka()
        elif izbor==5:
            ispis_grupa_zadataka()
        elif izbor==0:
            break
        else:
            print("Nevažeći odabir. Molimo pokušajte ponovno.")                        



main()


    

    

