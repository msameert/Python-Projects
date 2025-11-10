import sqlite3

# Connect to database with the name
connection = sqlite3.connect('student.db')

# Connecting to Cursor 
c = connection.cursor()
connection.execute("PRAGMA foreign_keys=ON")
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
#c.execute("SELECT rowid,* FROM students ORDER BY semester")

#print("NO. \tNAME \t\t GPA \t\tDEPARTMENT  \t SEMESTER")
#print("---------------------------------------------------------------------")
#for rowid, name, gpa, semester, department in c.fetchall():
 #   print(f"{rowid} \t{name}\t\t{gpa}\t{department}\t{semester}")
c.execute("""CREATE TABLE users (
          user_id INTEGER PRIMARY KEY AUTOINCREMENT,
          username text UNIQUE NOT NULL,
          password_hash text NOT NULL,
          role text NOT NULL CHECK (role IN('admin','student','faculty')),
          is_active INTEGER DEFAULT 1,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at DATETIME,
          created_by INTEGER,
          updated_by INTEGER,
          Foreign key (created_by) REFERENCES users(user_id),
          Foreign key (updated_by) REFERENCES users(user_id)
          )""")

c.execute("""CREATE TABLE departments (
          department_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name text UNIQUE NOT NULL,
          code text UNIQUE NOT NULL,
          head_id INTEGER,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at DATETIME,
          Foreign key (head_id) REFERENCES faculty(faculty_id) ON DELETE SET NULL
          )""")

c.execute("""CREATE TABLE faculty (
          faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name text,
          email text,
          designation text,
          is_active INTEGER DEFAULT 1,
          user_id INTEGER,
          department_id INTEGER,
          Foreign key (user_id) REFERENCES users(user_id),
          Foreign key (department_id) REFERENCES departments(department_id)
          )""")

c.execute("""CREATE TABLE semesters (
          semester_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name text,
          start_date text,
          end_date text,
          is_current INTEGER DEFAULT 1
          )""")

c.execute("""CREATE TABLE courses(
          course_id INTEGER PRIMARY KEY AUTOINCREMENT,
          course_code text UNIQUE NOT NULL,
          name text,
          credit_hours INTEGER NOT NULL,
          department_id INTEGER,
          faculty_id INTEGER,
          Foreign key (department_id) REFERENCES departments(department_id),
          Foreign key (faculty_id) REFERENCES faculty(faculty_id)
          )""")

c.execute("""CREATE TABLE students (
          student_id INTEGER PRIMARY KEY AUTOINCREMENT,
          student_code text UNIQUE NOT NULL,
          first_name text,
          last_name text,
          email text,
          enroll_year INTEGER NOT NULL,
          status text DEFAULT 'active' CHECK(status IN('active', 'graduated', 'suspended', 'withdrawn')),
          is_deleted INTEGER DEFAULT 0,
          deleted_at DATETIME,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at DATETIME,
          user_id INTEGER,
          department_id INTEGER,
          current_semester_id INTEGER,
          Foreign key (user_id) REFERENCES users(user_id),
          Foreign key (department_id) REFERENCES departments(department_id),
          Foreign key (current_semester_id) REFERENCES semesters(semester_id)
          )""") 

c.execute("""CREATE TABLE enrollments (
          enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
          enrollment_date text,
          status text DEFAULT 'enrolled' CHECK(status IN('enrolled','dropped','completed')),
          dropped_at DATETIME,
          updated_at DATETIME,
          student_id INTEGER,
          course_id INTEGER,
          semester_id INTEGER,
          Foreign key (student_id) REFERENCES students(student_id),
          Foreign key (course_id) REFERENCES courses(course_id),
          Foreign key (semester_id) REFERENCES semesters(semester_id)
          )""")

c.execute("""CREATE TABLE grades (
          grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
          marks_obtained REAL CHECK (marks_obtained >= 0 AND marks_obtained <= 100),
          grade_letter   TEXT CHECK (grade_letter IN ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F')),
          grade_points   REAL CHECK (grade_points >= 0 AND grade_points <= 4.0),
          gpa            REAL GENERATED ALWAYS AS (grade_points) STORED,
          remarks text,
          graded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
          created_at     DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at     DATETIME,
          graded_by INTEGER,
          enrollment_id INTEGER UNIQUE NOT NULL,
          Foreign key (graded_by) REFERENCES faculty(faculty_id),
          Foreign key (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
          )""")

                            # Insert users
#c.execute("""
#    INSERT INTO users (username, password_hash, role)
#    VALUES 
#    ('admin', 'hashed_admin_pass', 'admin'),
#    ('msameert', 'hashed_student_pass', 'student')
#    """)

                            # Insert departments
#c.execute("""
#          INSERT INTO departments (name,code)
#          VALUES
#          ('Computer Science', 'CS'),
#          ('Software Enginnering', 'SE')
#          """)
c.execute("""
          INSERT INTO users (username, password_hash,role)
          VALUES 
          ('zain123','pass_zain','faculty')""")

c.execute("""
                    INSERT INTO faculty (name, email, designation, user_id, department_id)
                    VALUES (
                        'Sir Zain',
                        'zainmughal@gmail.com',
                        'Professor',
                        (SELECT user_id FROM users WHERE username = 'zain123'),
                        (SELECT department_id FROM departments WHERE code = 'CS')
                    )""")
c.execute("""
            INSERT INTO students (student_code, first_name, last_name, email, enroll_year, user_id,department_id)
          VALUES ('SE-2025-0010','Muhammad','Sameer','msameert123@gmail.com','2025',(SELECT user_id FROM users WHERE username = 'msameert'),(SELECT department_id FROM departments WHERE code = 'SE'))""")

# this commits
connection.commit()
connection.close()

# To uuse database in app - we wrap the database code in functions and use it on other files - 
# like in one file the function is show_all() which has the code of showing record -

# and on the other file use function name with database like database.show_all()




