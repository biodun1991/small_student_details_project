import sqlite3
from datetime import datetime
import random
import re




# conn = sqlite3.connect('mydata.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM student_info WHERE matric_number = ?", ('SA4520618',))
# cursor.execute("""CREATE TABLE student_info(first_name TEXT,last_name TEXT,dob TEXT,gender TEXT,faculty TEXT,department TEXT,year TEXT,matric_number TEXT PRIMARY KEY) """)
# cursor.execute('''
# ALTER TABLE student_info ADD COLUMN dob TEXT
# ''')
# cursor.execute('''
# DROP TABLE IF EXISTS student_info
# ''')
# conn.commit()
# conn.close()


# this lines of code define functions  that takes list of all faculties as argument
def choose_faculty(faculties):
    for i in range(len(faculties)):
        print(f"({chr(97+i)}) {faculties[i]}")
    faculty_choice = (input('Selecet your faculty from the options above: ').lower()).strip()
    for i in range(len(faculties)):
        if faculty_choice == f"{chr(97+i)}":
            Faculty = faculties[i]
            return Faculty

# this lines of code define functions  that takes list of all departments as argument
def choose_department(departments):
    for i in range(len(departments)):
        print(f"({chr(97+i)}) {departments[i]}")
    department_choice = (input('Select your department from the options above: ').lower()).strip()
    for i in range(len(departments)):
        if department_choice == f"{chr(97+i)}":
            Department = departments[i]
            return Department

# This is a function that checks if input field is not empty
def empty_input_check(prompt):
    """Helper function to get non-empty input from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")

# This function insert data into the database
def insertData():
    firstName = empty_input_check('Enter your first name: ').capitalize()
    lastName = empty_input_check('Enter your last name: ').capitalize()
    Dob   = empty_input_check('Enter your date of birth in this format dd/mm/yyyy: ')
    Gender = empty_input_check('Are a Male or Female: ').capitalize()
    all_faculty = ['Faculty of Arts','Faculty of Science','Faculty of Engineering',
               'Faculty of Business Administration','Faculty of Law','Faculty of Agriculture','Faculty of Medicine','Faculty of Pharmacy'
    
                 ]
    # the choose_faculty function is called here because we want equate variable faculty to the choice of the student
    Faculty = choose_faculty(all_faculty)
    all_department = ['Department of English','Department of Mathematics','Department of International Law',      'Department of Educational Administration','Department of Food Science','Department of Anatomy','Department of Medicine','Department of Pharmaceutical Chemistry','Department of Environmental Management','Department of Public Law'
               ]
    # the choose_department function is called here because we want equate variable Department to the choice of the student
    Department = choose_department(all_department)
  
    Year = datetime.now().year
    random_numbers = random.sample(range(0, 9), 7)
    rand = "".join(map(str, random_numbers))
    matricNumber = firstName[0] + lastName[0] + rand
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO student_info(first_name,last_name,dob,gender,faculty,department,year,matric_number)VALUES(?,?,?,?,?,?,?,?)""",(firstName,lastName,Dob,Gender,Faculty,Department,Year,matricNumber))
    conn.commit()
    conn.close()

# this function is fetching matric number from the database using faculty
def dataByfaculty(Faculty):
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT matric_number FROM student_info WHERE faculty=?',(Faculty,))    
    rows = cursor.fetchall()
    if rows:
       for row in rows:
           print(row[0])
    else:
        print("No matric number found with that faculty")
    conn.commit()
    conn.close()


# this function is fetching matric number from the database using department
def dataByDepartment(department):
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT matric_number FROM student_info WHERE department=?',(department,))    
    rows = cursor.fetchall()
    if rows:
       for row in rows:
           print(row[0])
    else:
        print("No matric number found with that department")
    conn.commit()
    conn.close()


# this function is fetching matric number from the database using year of admission
def dataByYear(year):
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT matric_number FROM student_info WHERE year=?',(year,))    
    rows = cursor.fetchall()
    if rows:
       for row in rows:
           print(row[0])
    else:
        print("No matric number found with that year")
    conn.commit()
    conn.close()


# this function is fetching matric number from the database using date of birth
def dataByDateOfBirth(dob):
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT matric_number FROM student_info WHERE dob=?',(dob,))    
    rows = cursor.fetchall()
    if rows:
       for row in rows:
           print(row[0])
    else:
        print("No matric number found with that date of birth")
    conn.commit()
    conn.close()


# this function is fetching all matric number from the database
def viewAllMatric():
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    cursor.execute('SELECT matric_number FROM student_info')
    rows = cursor.fetchall()
    if rows:
       for row in rows:
           print(row[0])
    else:
        print("Database is empty")
    conn.commit()
    conn.close()



# this function is fetching all data from the database sort by faculty
def orderByFaculty():
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_info ORDER BY faculty')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# this function is fetching all data from the database sort by department
def orderByDepartment():
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_info ORDER BY department')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# this function is fetching all data from the database sort by year of admission
def orderByYear():
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_info ORDER BY year')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# def deleteTable():
#     conn = sqlite3.connect("mydata.db")
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM student_info')
#     conn.commit()
#     conn.close()

# this function is taking care of all what the student can do on the app
def student(studentcando):
    print('Choose from the options below what you want to do')
    for i in range(len(studentcando)):
        print(f"({chr(97+i)}) {studentcando[i]}")
    choice = (input('Enter your option here: ').lower()).strip()
    for i in range(len(studentcando)):
        if choice == f"{chr(97+i)}":
            student_choice = studentcando[i]
            if student_choice == "Insert data":
                insertData()
            elif student_choice == "Get matric number":
                 firstName = empty_input_check('Enter your first name: ').capitalize()
                 lastName = empty_input_check('Enter your last name: ').capitalize()
                 Dob   = empty_input_check('Enter your date of birth in this format dd/mm/yyyy: ')
                 Gender = empty_input_check('Are a Male or Female: ').capitalize()
                 all_faculty = ['Faculty of Arts','Faculty of Science','Faculty of Engineering',
                 'Faculty of Business Administration','Faculty of Law','Faculty of Agriculture','Faculty of Medicine','Faculty of Pharmacy'
                 ]
                 Faculty = choose_faculty(all_faculty)
                 all_department = ['Department of English','Department of Mathematics','Department of International Law',      'Department of Educational Administration','Department of Food Science','Department of Anatomy','Department of Medicine','Department of Pharmaceutical Chemistry','Department of Environmental Management','Department of Public Law'
                 ]
                 Department = choose_department(all_department)
                 Year = datetime.now().year
                 conn = sqlite3.connect('mydata.db')
                 cursor = conn.cursor()
                 cursor.execute("""SELECT matric_number FROM student_info WHERE first_name=? AND last_name=? AND dob=? AND gender=? AND faculty=? AND department=? AND year=?""",(firstName,lastName,Dob,Gender,Faculty,Department,Year))
                 result= cursor.fetchone()
                 if result:
                    for val in result:
                        print(val)
                 else:
                    print("No matric number found for that info")
            elif student_choice == "View matric numbers by Date of Birth":
                  dob = input('Enter date of birth in this format dd/mm/yyyy: ')
                  dataByDateOfBirth(dob)
            elif student_choice == "View matric numbers by faculty":
                  all_faculty = ['Faculty of Arts','Faculty of Science','Faculty of Engineering',
                  'Faculty of Business Administration','Faculty of Law','Faculty of Agriculture','Faculty of Medicine','Faculty of Pharmacy'
                   ]
                  Faculty = choose_faculty(all_faculty)
                  dataByfaculty(Faculty)
            elif student_choice == "View matric numbers by department":
                  all_department = ['Department of English','Department of Mathematics','Department of International Law',      'Department of Educational Administration','Department of Food Science','Department of Anatomy','Department of Medicine','Department of Pharmaceutical Chemistry','Department of Environmental Management','Department of Public Law'
                  ]
                  Department = choose_faculty(all_department)
                  dataByDepartment(Department)
            elif student_choice == "View matric numbers by Year of admission":
                while True:
                   user_input = input("Enter year: ").strip()
    
                   if user_input == '':
                       print("Input cannot be empty")
                   elif user_input.isdigit():
                         year = int(user_input)
                         dataByYear(year)
                         break
                   else:
                         print("Input must be numbers")
                  

# this function is taking care of all what the admin can do on the app
def admin(admincando):
    print('Choose from the options below what you want to do')
    for i in range(len(admincando)):
        print(f"({chr(97+i)}) {admincando[i]}")
    choice = (input('Enter your option here: ').lower()).strip()
    for i in range(len(admincando)):
        if choice == f"{chr(97+i)}":
            admin_choice = admincando[i]
    if admin_choice == "View all matric numbers":
        viewAllMatric()
    elif admin_choice == "View matric numbers sorted by faculty":
        orderByFaculty()
    elif admin_choice == "View matric numbers sorted by department":
        orderByDepartment()
    elif admin_choice == "View matric numbers sorted by year of admission":
         orderByYear

what_student_can_do = ['Insert data','Get matric number','View matric numbers by Date of Birth','View matric numbers by faculty','View matric numbers by department','View matric numbers by Year of admission']
what_admin_can_do =['View all matric numbers','View matric numbers sorted by faculty','View matric numbers sorted by department','View matric numbers sorted by year of admission']

print('Welcome to the School portal')

while True:
    user = (input("Are you student or an Administrator? type s for student and a for admin: ").lower()).strip()
    if user == 's':
        student(what_student_can_do)
        break
    elif user == 'a':
          admin(what_admin_can_do)
          break
    else:
        print("invalid input")

