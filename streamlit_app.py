import sqlite3

def save_to_database(name, email, age, gender):
    # Adatbázis kapcsolat létrehozása (ha még nem létezik, létrehozza)
    conn = sqlite3.connect("adatok.db")

    # Cursor létrehozása
    cursor = conn.cursor()

    # Tábla létrehozása, ha még nem létezik
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS felhasznalok (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nev TEXT,
            email TEXT,
            eletkor INTEGER,
            nem TEXT
        )
    ''')

    # Adatok beszúrása
    cursor.execute('''
        INSERT INTO felhasznalok (nev, email, eletkor, nem)
        VALUES (?, ?, ?, ?)
    ''', (name, email, age, gender))

    # Tranzakció lezárása és mentése
    conn.commit()

    # Kapcsolat lezárása
    conn.close()

# Teszt adatok
nev = "John Doe"
email = "john.doe@example.com"
eletkor = 25
nem = "Ferfi"

# Adatok beszúrása az adatbázisba
save_to_database(nev, email, eletkor, nem)
