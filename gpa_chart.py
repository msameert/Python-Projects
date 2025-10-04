"""GPA calculation along with Data Visualization"""

import numpy as np
import matplotlib.pyplot as plt


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

grade_array = np.array(grades, dtype=str)

gpa = calculate_gpa(grades)
print("Your GPA is :", round(gpa,2))

"""----Visualization Section---"""

fig, axes = plt.subplots(1,3, figsize=(16,5))

subject_names = ["PF", "ICT", "Discrete", "English", "Calculus", "PF Lab", "ICT Lab"]
axes[0].set_xlabel("Subjects")
axes[0].set_ylabel("Marks")
axes[0].set_title("Marks per Subject")
axes[0].plot(subject_names, marks, marker ="o")

axes[2].bar(["GPA"],[gpa])
axes[2].set_ylim(0,4.0)
axes[2].set_title("GPA")
axes[2].set_ylabel("GPA Value")

unique_grades, counts = np.unique(grade_array, return_counts=True)
axes[1].set_title("Grade Distribution")
axes[1].pie(counts, labels=unique_grades, startangle=90, autopct="%1.1f%%", colors=plt.cm.Paired.colors)

plt.tight_layout()
plt.show()

