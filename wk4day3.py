import sqlite3

conn = sqlite3.connect("students.db")

c = conn.cursor()

#c.execute(""" CREATE TABLE Students_Data(
 #   first_name TEXT,
  #  last_name  TEXT,
   # email TEXT
    #)""")


#print("successful")

#Students_List = [
 #                ("Tayo","johnson","tayojohnson@email.com"),
  #               ("seyi","williams","seyi@gmail.com"),
   #              ("doyin","tajudeen","doyintaju@gmail.com")
#]

#c.executemany("INSERT INTO Students_info VALUES (?,?,?)", Students_List)

#conn.commit()

#print("succesful")

#query the database
#c.execute("SELECT * FROM students_info")

#item = c.fetchall()
#print('First_name' + '\t\tlast_name' + '\t\temail')
#print('-----------' + '\t\t--------' + '\t\t------')

#for item in item:
#    print(item[0] + " \t\t\t " + item[1] + " \t\t\t " + item[2])

#conn.commit()


#c.execute("ALTER TABLE Students_Data RENAME TO students_Info")

#conn.commit()
print("success")

#c.execute("ALTER TABLE students_info ADD COLUMN course")

#conn.execute("""UPDATE students_info SET course = "data_science" """)

#conn.commit()
#print("successful")

c.execute("SELECT * FROM students_info")

items = c.fetchall()
print('First name' + '\t\tlastname' + '\t\temail' + 't\t\t\t\tcourse')
print('----------' + '\t\t----' + '\t\t------' +'\t\t\t\t\t------')

for item in items:
    print(item[0] + " \t\t\t " + item[1] + " \t\t\t " + item[3])

c.execute("DELETE FROM students_info WHERE last_name = 'williams' ")

c.execute("UPDATE students_info SET last_name = 'surname' ")

print("success")
conn.commit()
conn.close()