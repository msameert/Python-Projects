def get_grades(score) :
    if score >= 85 :
        return "A"
    elif score >= 80 :
        return "A-"
    elif score >= 75 :
        return "B+"
    elif score >= 71 :
        return "B"
    elif score >= 68 :
        return "B-"
    elif score >= 64 :
        return "C+"
    elif score >= 61 :
        return "C"
    elif score >= 58 :
        return "C-"
    elif score >= 54 :
        return "D+"
    elif score >= 50 :
        return "D"
    else :
        return "F"
    
def calculate_gpa(grade_list):
    grade_points = {
        "A": 4.0,
        "A-": 3.66,
        "B+": 3.33,
        "B": 3.00,
        "B-": 2.66,
        "C+": 2.33,
        "C": 2.00,
        "C-": 1.66,
        "D+": 1.33,
        "D": 1.00,
        "F": 0.00
    }

    total_points = 0
    for grade in grade_list :
         total_points += grade_points[grade]

    return total_points/len(grade_list)

    

marks1 = float(input("Enter your PF marks : "))
marks2 = float(input("Enter your ICT marks : "))
marks3 = float(input("Enter your Discrete marks : "))
marks4 = float(input("Enter your English marks : "))
marks5 = float(input("Enter your Calculus marks : "))
marks6 = float(input("Enter your PF Lab marks : "))
marks7 = float(input("Enter your ICT Lab marks : "))

marks = [marks1,marks2,marks3,marks4,marks5,marks6,marks7]



grades = []
for score in marks :
    grades.append(get_grades(score))

print("Your Grades are : ", grades)



gpa = calculate_gpa(grades)
print("Your GPA is :", round(gpa,2))
