import sys
from time import sleep

import psycopg2


def backup():
    con = None

    sql = [
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';",
        "SELECT * FROM"
    ]

    tables = []

    try:
        con = psycopg2.connect(host='database', database='postgres',
                               user='postgres', password='postgres')
        cur = con.cursor()
        cur.execute(sql[0])
        for row in cur:
            tables.append(row[0])

            # f.write("insert into auth_user values (" + str(row) + ");")

    except psycopg2.DatabaseError as e:
        print(f'Backup Error {e}')
        sys.exit(1)

    finally:
        if con:
            con.close()

    for i in tables:
        if i in ['auth_group_permissions', 'auth_group', 'auth_permission', 'auth_user_groups', 'auth_user_user_permissions', 'django_content_type', 'django_migrations']:
            pass

        else:
            f = open(f'./tables/{i}.csv', 'w')

            try:
                con = psycopg2.connect(host='database', database='postgres',
                                       user='postgres', password='postgres')
                cur = con.cursor()
                cur.execute(f"{sql[1]} {i}")

                for row in cur:
                    row = str(row).replace(', ', ';')
                    f.write(f"{row[1:-1:]}\n")

                f.close()

            except psycopg2.DatabaseError as e:
                print(f'Backup Error {e}')
                sys.exit(1)

            finally:
                if con:
                    con.close()


while True:
    print("Realizando Backup das Tabelas")
    backup()
    print("Backup Realizado")
    sleep(10800)
