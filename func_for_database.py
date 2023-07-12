def del_tables(connect):
    """Функция удаляет таблицы с БД."""
    with connect.cursor() as cur:
        cur.execute("""
        DROP TABLE phone;
        DROP TABLE client;
        """)
        connect.commit()


def create_tables(connect):
    """Функция, создающая структуру БД (таблицы)."""
    with connect.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            client_id      SERIAL PRIMARY KEY,
            client_name    VARCHAR(30) NOT NULL,
            client_surname VARCHAR(30) NOT NULL,
            client_email   VARCHAR(40) UNIQUE NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone(
            phone_id     SERIAL PRIMARY KEY,
            client_id    INTEGER REFERENCES client(client_id),
            phone_number VARCHAR(20) UNIQUE NOT NULL
        );    
        """)
        connect.commit()


def add_client(connect, first_name, last_name, email, phone=None):
    """Функция, позволяющая добавить нового клиента."""
    with connect.cursor() as cur:
        cur.execute("""
        INSERT INTO client(client_name, client_surname, client_email)
        VALUES (%s, %s, %s)
        RETURNING client_id;
        """, (first_name, last_name, email))
        client_id = cur.fetchone()
        if phone is None:
            return
        else:
            cur.execute("""
            INSERT INTO phone(client_id, phone_number)
            VALUES (%s, %s);
            """, (client_id, phone))
            connect.commit()


def add_phone(connect, client_id, phone):
    """Функция, позволяющая добавить телефон для существующего клиента."""
    with connect.cursor() as cur:
        cur.execute("""
        INSERT INTO phone(client_id, phone_number)
        VALUES (%s, %s);
        """, (client_id, phone))
        connect.commit()


def change_data_client(connect, client_id, first_name=None, last_name=None, email=None, phone=None):
    """Функция, позволяющая изменить данные о клиенте."""
    with connect.cursor() as cur:
        cur.execute("""
        SELECT * FROM client
         WHERE client_id = %s;
        """, (client_id,))
        client_data = cur.fetchone()
        if first_name is None:
            first_name = client_data[1]
        if last_name is None:
            last_name = client_data[2]
        if email is None:
            email = client_data[3]
        cur.execute("""
        UPDATE client
           SET client_name = %s, client_surname = %s, client_email = %s
         WHERE client_id = %s;
        """, (first_name, last_name, email, client_id))
        connect.commit()
        if phone is not None:
            add_phone(connect, client_id, phone)


def del_phone(connect, client_id, phone=None):
    """Функция, позволяющая удалить телефон для существующего клиента."""
    with connect.cursor() as cur:
        if phone is not None:
            cur.execute("""
            DELETE FROM phone
             WHERE client_id = %s AND phone_number = %s;
            """, (client_id, phone))
            connect.commit()
        else:
            cur.execute("""
            DELETE FROM phone
             WHERE client_id = %s;
            """, (client_id,))
            connect.commit()


def del_client(connect, client_id):
    """Функция, позволяющая удалить существующего клиента."""
    with connect.cursor() as cur:
        del_phone(connect, client_id)
        cur.execute("""
        DELETE FROM client
         WHERE client_id = %s;
        """, (client_id,))
        connect.commit()


def find_client(connect, first_name=None, last_name=None, email=None, phone=None):
    """Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону."""
    with connect.cursor() as cur:
        if email is not None or phone is not None:
            cur.execute("""
            SELECT c.client_id
              FROM client AS c
              JOIN phone AS p
                ON c.client_id = p.client_id
             WHERE client_email = %s OR phone_number = %s;
            """, (email, phone))
        elif first_name is not None and last_name is not None:
            cur.execute("""
            SELECT client_id
              FROM client
             WHERE client_name = %s AND client_surname = %s;
            """, (first_name, last_name))
        elif first_name is not None or last_name is not None:
            cur.execute("""
            SELECT client_id
              FROM client
             WHERE client_name = %s OR client_surname = %s;
            """, (first_name, last_name))
        client_id = cur.fetchall()
        client_info(connect, client_id)


def client_info(connect, client_id):
    """Функция выводит информацию о клиенте по его идентификатору."""
    for val in client_id:
        for i in val:
            with connect.cursor() as cur:
                cur.execute("""
                    SELECT client_id, client_name, client_surname, client_email
                      FROM client
                     WHERE client_id = %s;
                    """, (i,))
                data_client = cur.fetchone()
                print(f'ID: {data_client[0]}\nИмя: {data_client[1]}\n'
                      f'Фамилия: {data_client[2]}\nemail: {data_client[3]}')
                cur.execute("""
                    SELECT phone_number
                      FROM phone
                     WHERE client_id = %s;
                    """, (i,))
                phone_client = cur.fetchall()
                print(f'Телефон(ы): {", ".join([n for num in phone_client for n in num])}\n')

