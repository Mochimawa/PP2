import psycopg2
from config import load_config

def create_table():
    params = load_config()  # читаем параметры из database.ini
    conn = None
    try:
        conn = psycopg2.connect(**params)   # подключение
        cur = conn.cursor()                 # создаём курсор

        # SQL‑команда: создаём таблицу, если её ещё нет
        cur.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INTEGER
            );
        """)

        conn.commit()   # фиксируем изменения

        print("Таблица created (если её не было).")

        cur.close()     # закрываем курсор
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка:", error)
    finally:
        if conn:
            conn.close()  # закрываем соединение
            print("Соединение закрыто.")

if __name__ == '__main__':
    create_table()
