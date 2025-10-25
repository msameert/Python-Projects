import sqlite3

# Connect to database with the name
connection = sqlite3.connect('student.db')

# Connecting to Cursor 
c = connection.cursor()
# Now we can use C as our Cursor to give commands

# Create a Table 
#c.execute("""CREATE TABLE students (
#          name text,
#          GPA real, # DEFAULT 'undecided' - this is if we don't add something in specific row then it will show default value.
#          semester text,
#          department text
#   )""")

# INSERT a student
#c.execute("INSERT INTO students VALUES ('Sameer', '3.5', '2nd', 'Software Engineering')")

# Data type:
# 1. text 2. real (decimals) 3.integer 4. null 5. blob

#c.execute("INSERT INTO students VALUES ('Samuel', '3.4', '3rd', 'Computer Engineering')")

# This is how to change record
#c.execute("""UPDATE students SET GPA = 3.2 
#          WHERE name = 'John' 
#          """)

# This Deletes 
#c.execute("DELETE from students WHERE rowid IN (3, 4, 5, 6, 7)")

#SELECT name FROM students WHERE name LIKE 'jo%'    - it selects names which starts from jo

# This selects all - * means ALL, while rowid is numbers, also ordered the output
c.execute("SELECT rowid,* FROM students ORDER BY semester")

print("NO. \tNAME \t\t GPA \t\tDEPARTMENT  \t SEMESTER")
print("---------------------------------------------------------------------")
for rowid, name, gpa, semester, department in c.fetchall():
    print(f"{rowid} \t{name}\t\t{gpa}\t{department}\t{semester}")


# this commits
connection.commit()
connection.close()

# To uuse database in app - we wrap the database code in functions and use it on other files - 
# like in one file the function is show_all() which has the code of showing record -

# and on the other file use function name with database like database.show_all()

