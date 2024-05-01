import psycopg2 as pgsql
import csv
conn=pgsql.connect(
    host='localhost', 
    dbname='PhoneBookSecond', 
    user='postgres', 
    password='7079630'
)
cur=conn.cursor()

# Create a new table
cur.execute("""CREATE TABLE phones_data (
            name VARCHAR(255),
            surname VARCHAR(255),
            phone_number VARCHAR(20) PRIMARY KEY
);
""")

conn.commit()

#upload data from csv file
filename = r'C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab11\people.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, surname, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phones_data (name, surname, phone_number) VALUES 
                    ('{name}', '{surname}', '{phone_number}');
        """)

        conn.commit()

#1 Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)

cur.execute("SELECT * FROM phones_data WHERE phone_number LIKE '+7777%'")
print(cur.fetchall())

#2 Create procedure to insert new user by name and phone, update phone if user already exists
cur.execute("""
    CREATE OR REPLACE PROCEDURE public.insert_or_update_user(a VARCHAR, b VARCHAR, c VARCHAR)
    LANGUAGE plpgsql
    AS $$
    DECLARE 
        v_exists INTEGER;
    BEGIN
        SELECT count(*) INTO v_exists FROM public.phones_data WHERE name = a AND surname = b;
        IF v_exists = 0 THEN
            INSERT INTO public.phones_data (name, surname, phone_number) VALUES (a, b, c);
        ELSE
            UPDATE public.phones_data SET phone_number = c WHERE name = a AND surname = b;
        END IF;
    END;
    $$;
""")

#5 Implement procedure to deleting data from tables by username or phone
cur.execute("""
    CREATE OR REPLACE PROCEDURE public.delete_user(a VARCHAR, b VARCHAR)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM public.phones_data WHERE name = a AND surname = b;
    END;
    $$;
""")


# Executing the insert_or_update_user procedure
cur.execute("""CALL public.insert_or_update_user('Leo','Messi','+77075552020')""")

# Executing the delete_user procedure
cur.execute("""CALL public.delete_user('Cristiano', 'Ronaldo')""")

conn.commit()