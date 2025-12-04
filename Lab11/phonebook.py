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

def upsert_contact():
    print("\nAdd or Update Contact:")
    first_name = input("First Name: ")
    last_name = input("Last Name (optional): ") or None
    phone_number = input("Phone Number: ")
    
    if not first_name or not phone_number:
        print("Name and Phone are required.")
        return

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_or_update_contact(%s, %s, %s)", (first_name, last_name, phone_number))
                conn.commit()
        print("Contact processed successfully (Inserted or Updated).")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error calling procedure: {error}")

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

def delete_contact_proc():
    identifier = input("\nEnter First Name or Phone Number to delete: ")
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                
                cur.execute("CALL delete_contact_by_info(%s)", (identifier,))
                conn.commit()
        print("Delete procedure executed.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Delete error: {error}")

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
        elif choice == '2': upsert_contact()
        elif choice == '3': bulk_insert_contacts()
        elif choice == '4': query_with_pagination()
        elif choice == '5': delete_contact_proc()
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    phone_book_menu()