from func_for_database import *
import psycopg2


if __name__ == '__main__':
    with psycopg2.connect(database="homework_5", user="postgres", password="159632") as conn:
        # # Удаление таблиц с БД
        # del_tables(conn)

        # 1. Создание таблиц в БД
        create_tables(conn)

        # 2. Добавление новых клиентов в БД
        # add_client(conn, first_name='Андрей', last_name='Бурцев', email='bur@mail.ru', phone='89274537642')
        # add_client(conn, first_name='Александр', last_name='Ильин', email='alex@mail.ru', phone='89276536747')
        # add_client(conn, first_name='Роман', last_name='Матвеев', email='matveev@mail.ru', phone='89279405743')
        # add_client(conn, first_name='Вадим', last_name='Григорьев', email='vad@mail.ru', phone='89276704512')
        # add_client(conn, first_name='Александр', last_name='Пахомов', email='paxomov@mail.ru')
        # add_client(conn, first_name='Игорь', last_name='Сергеев', email='serg@mail.ru')
        # add_client(conn, first_name='Анастасия', last_name='Данилова', email='danilova@mail.ru')

        # # 3. Добавление телефона клиенту
        # add_phone(conn, client_id=4, phone='89275430072')
        # add_phone(conn, client_id=4, phone='89279531288')
        # add_phone(conn, client_id=3, phone='89276633178')
        # add_phone(conn, client_id=5, phone='89274580305')
        # add_phone(conn, client_id=1, phone='89279985511')
        # add_phone(conn, client_id=6, phone='89270236377')

        # # 4. Изменение данных клиента
        # change_data_client(conn, client_id=6, first_name='Николай', last_name='Фёдоров',
        #                    email='fedr@mail.ru', phone='89275461298')
        # change_data_client(conn, client_id=7, last_name='Иванова', email='ivanova@mail.ru')
        # change_data_client(conn, client_id=4, email='grigoriev@mail.ru')

        # # 5. Удаление телефона клиента
        # del_phone(conn, client_id=4, phone='89275430072')
        # del_phone(conn, client_id=2, phone='89276536747')
        # del_phone(conn, client_id=1, phone='89274537642')

        # # 6. Удалить клиента с БД
        # del_client(conn, client_id=6)

        # 7. Найти клиента(клиентов) по ID
        # find_client(conn, first_name='Александр', last_name='Ильин')
        # find_client(conn, first_name='Александр')
        # find_client(conn, first_name='Вадим', phone='89276704512')

    conn.close()
