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


def bulk_insert_contacts():
    print("\nBulk Insert Mode.")
    print("Enter contacts separated by comma (Name,Phone). Type 'done' to finish.")
    
    names = []
    phones = []
    
    while True:
        entry = input("Entry (Name,Phone): ")
        if entry.lower() == 'done':
            break
        try:
            name, phone = entry.split(',')
            names.append(name.strip())
            phones.append(phone.strip())
        except ValueError:
            print("Invalid format. Use 'Name,Phone'")

    if not names:
        return

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_many_contacts(%s, %s, %s)", (names, phones, []))
                result = cur.fetchone()
                invalid_data = result[0] if result else []
                conn.commit()
                
        print("\nBatch processing complete.")
        if invalid_data:
            print("The following data was INVALID and not inserted:")
            for item in invalid_data:
                print(f"- {item}")
        else:
            print("All data inserted successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Bulk insert error: {error}")

def query_with_pagination():
    try:
        limit = int(input("\nEnter limit (how many records): "))
        offset = int(input("Enter offset (skip how many): "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    sql = "SELECT contact_id, first_name, last_name, phone_number FROM phone_book ORDER BY contact_id LIMIT %s OFFSET %s"
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit, offset))
                rows = cur.fetchall()
                
                print(f"\n--- Page (Limit: {limit}, Offset: {offset}) ---")
                if not rows:
                    print("No more records.")
                for row in rows:
                    print(f"ID: {row[0]} | {row[1]} {row[2] or ''} | {row[3]}")
                    
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Pagination query error: {error}")

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
        print("\n--- Advanced Phone Book (PostgreSQL) ---")
        print("1. Find contacts (Pattern Search)")
        print("2. Add/Update Contact (Stored Procedure)")
        print("3. Bulk Insert (Stored Procedure with Loop/Check)")
        print("4. View Contacts with Pagination")
        print("5. Delete Contact (Stored Procedure)")
        print("exit - to close the program")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1': query_contacts()
        elif choice == '2':  update_contact()
        elif choice == '3': bulk_insert_contacts()
        elif choice == '4': query_with_pagination()
        elif choice == '5': delete_contact()
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    phone_book_menu()