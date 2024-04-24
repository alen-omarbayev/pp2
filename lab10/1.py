import psycopg2
import csv
# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='PhoneBook', 
    user='postgres', 
    password='7079630'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# Delete table
cur.execute('DROP TABLE phones_data;')

conn.commit()

#1
# Create a new table
cur.execute("""CREATE TABLE phones_data (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")

conn.commit()

#2
#upload data from csv file
filename = r'C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab10\people.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, id, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phones_data (name, id, phone_number) VALUES 
                    ('{name}', '{id}', '{phone_number}');
        """)

        conn.commit()
#entering user name, phone from console
kboard_name = str(input("Name: "))
kboard_id = int(id)+1
num = str(input("Num: "))

postgres_insert_query = """ INSERT INTO  phones_data (name, id, phone_number) VALUES (%s,%s,%s)"""
record_to_insert = (kboard_name, kboard_id, num)
cur.execute(postgres_insert_query, record_to_insert)

conn.commit()

#3 Implement updating data in the table (change user first name or phone)

cur.execute("""UPDATE phones_data
            SET name = '(changed)'
            WHERE phone_number = '+77777777777';
""")

conn.commit()

#4 Querying data from the tables (with different filters)

cur.execute("SELECT * FROM phones_data WHERE name = 'Alen'")
print(cur.fetchall())

#5 Implement deleting data from tables by username of phone

cur.execute("""DELETE FROM phones_data
            WHERE name = 'Lebron';
""")

conn.commit()
