""" Using File Handling to manage and store Student result Data """


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

student_name = input("Enter your name : ")
marks = []
subjects = ["PF", "ICT", "Discrete", "Calculus", "English", "PF Lab", "ICT Lab"]

for subject in subjects:
    score = float(input(f"Enter your {subject} marks :"))
    marks.append(score)

grades = [get_grades(score) for score in  marks]
print("Your grades are :", grades)

gpa = calculate_gpa(grades)
print("Your GPA is :", round(gpa, 2))

with open("results.txt", "w") as f:
    f.write(f"Student name is :{student_name}\n")
    f.write("Student Results : ")
    for i in range(len(subjects)) :
        f.write(f"{subjects[i]}: {marks[i]} -> {grades[i]}\n")
    f.write(f"GPA is : {round(gpa, 2)}\n")
    f.write("-"*30 + "\n")

print("your result have been saved to file")


