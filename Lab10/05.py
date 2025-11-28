import psycopg2
import csv
from config import load_config

def create_table():
    """ Creates the phonebook table if it doesn't exist """
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit() 
        print("Table 'phonebook' is ready.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error creating table: {error}")

def insert_contact_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    sql = "INSERT INTO phonebook(name, phone) VALUES(%s, %s) RETURNING id;"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                new_id = cur.fetchone()[0]
                conn.commit()
                print(f"Contact {name} added with ID {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Insert error: {error}")

def insert_from_csv():
    filename = input("Enter CSV filename (e.g., phonebook.csv): ")
    
    data_list = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                data_list.append(row)
    except FileNotFoundError:
        print("File not found.")
        return

    sql = "INSERT INTO phonebook(name, phone) VALUES(%s, %s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, data_list)
                conn.commit()
                print(f"Loaded {len(data_list)} contacts from file.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"CSV Error: {error}")

def update_contact():
    name = input("Enter user name to update: ")
    new_phone = input("Enter NEW phone: ")

    sql = "UPDATE phonebook SET phone = %s WHERE name = %s"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone, name))
                conn.commit()
                
                if cur.rowcount > 0:
                    print(f"Phone for {name} updated.")
                else:
                    print(f"User {name} not found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Update error: {error}")

def get_contacts():
    filter_option = input("Filter by name? (y/n): ")
    
    sql = "SELECT id, name, phone FROM phonebook"
    params = ()

    if filter_option.lower() == 'y':
        part_name = input("Enter part of name: ")
        sql += " WHERE name LIKE %s"
        params = (f'%{part_name}%',)

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                rows = cur.fetchall()
                
                print("\n--- Phonebook ---")
                for row in rows:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
                print("-----------------\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Read error: {error}")

def delete_contact():
    identifier = input("Enter name or phone to delete: ")

    sql = "DELETE FROM phonebook WHERE name = %s OR phone = %s"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (identifier, identifier))
                conn.commit()
                if cur.rowcount > 0:
                    print(f"Deleted records: {cur.rowcount}")
                else:
                    print("Nothing found to delete.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Delete error: {error}")

if __name__ == '__main__':

    create_table()

    while True:
        print("\nChoose action:")
        print("1. Add from Console")
        print("2. Add from CSV file")
        print("3. Query data")
        print("4. Update data")
        print("5. Delete data")
        print("0. Exit")

        choice = input(">> ")

        if choice == '1':
            insert_contact_console()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            get_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid input, try again.")