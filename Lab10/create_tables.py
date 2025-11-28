import psycopg2
import csv
from config import load_config

def create_table():
    command = """
        CREATE TABLE IF NOT EXISTS phone_book (
            contact_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255),
            phone_number VARCHAR(20) NOT NULL UNIQUE
        )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database error: {error}")

def insert_from_csv(file_path):
    sql = "INSERT INTO phone_book(first_name, last_name, phone_number) VALUES (%s, %s, %s) ON CONFLICT (phone_number) DO NOTHING;"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        if row: cur.execute(sql, row)
                conn.commit()
        print(f"Data from {file_path} loaded successfully.")
    except Exception as error:
        print(f"Error while loading from CSV: {error}")

def insert_from_console():
    print("\nEnter new contact details:")
    first_name = input("First Name: ")
    last_name = input("Last Name (optional): ")
    phone_number = input("Phone Number: ")
    if not first_name or not phone_number:
        print("First name and phone number are required. Contact not added.")
        return
    sql = "INSERT INTO phone_book(first_name, last_name, phone_number) VALUES (%s, %s, %s)"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, last_name, phone_number))
                conn.commit()
        print("Contact added successfully!")
    except Exception as error:
        print(f"Could not add contact: {error}")

def query_contacts():
    filter_term = input("\nEnter name or phone to search (leave blank to show all): ")
    if filter_term:
        sql = "SELECT contact_id, first_name, last_name, phone_number FROM phone_book WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number ILIKE %s"
        params = (f"%{filter_term}%", f"%{filter_term}%", f"%{filter_term}%")
    else:
        sql = "SELECT contact_id, first_name, last_name, phone_number FROM phone_book ORDER BY first_name"
        params = None
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                rows = cur.fetchall()
                if not rows: print("No contacts found.")
                else:
                    print("\n--- Search Results ---")
                    for row in rows: print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")
    except Exception as error:
        print(f"Query failed: {error}")

def update_contact():
    search_term = input("Enter the first name of the contact to update: ")
    new_first_name = input("Enter new first name (or leave blank): ")
    new_phone = input("Enter new phone number (or leave blank): ")

    if not new_first_name and not new_phone:
        print("Nothing to update.")
        return

    query_parts = []
    params = []
    if new_first_name:
        query_parts.append("first_name = %s")
        params.append(new_first_name)
    if new_phone:
        query_parts.append("phone_number = %s")
        params.append(new_phone)
    
    params.append(search_term)
    
    sql = f"UPDATE phone_book SET {', '.join(query_parts)} WHERE first_name = %s"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(params))
                conn.commit()
                if cur.rowcount == 0: print("Contact not found.")
                else: print(f"Successfully updated {cur.rowcount} contact(s).")
    except Exception as error:
        print(f"Update failed: {error}")

def delete_contact():
    identifier = input("\nEnter first name or phone number to delete: ")
    sql = "DELETE FROM phone_book WHERE first_name = %s OR phone_number = %s"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (identifier, identifier))
                conn.commit()
                if cur.rowcount == 0: print("Contact not found.")
                else: print(f"Successfully deleted {cur.rowcount} contact(s).")
    except Exception as error:
        print(f"Delete failed: {error}")

def phone_book_menu():
    create_table()
    while True:
        print("\n--- Phone Book ---")
        print("1. Search contacts")
        print("2. Add new contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Load data from contacts.csv")
        print("exit - to close the program")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1': query_contacts()
        elif choice == '2': insert_from_console()
        elif choice == '3': update_contact()
        elif choice == '4': delete_contact()
        elif choice == '5': insert_from_csv('contacts.csv')
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    phone_book_menu()