# CGPA Calculator 

Semester = int(input("Enter Your Semester: "))

NoOfSubjects = int(input("Enter number of Subjects: "))

Total_GPA = 0
Total_credits = 0
for i in range(0 , NoOfSubjects):
    Subject_name = input(f"Enter the name of subject at position {i+1}: ")
    Subject_GPA = float(input(f"Enter the GPA of {Subject_name}: "))
    Credit_hour = int(input(f"Enter the credit hours of {Subject_name}: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    GPA_Cal = Subject_GPA * Credit_hour
    Total_GPA += GPA_Cal
    Total_credits += Credit_hour

TotalGPA = Total_GPA/Total_credits

def Grade(CGPA):
    if CGPA>= 3.7 and CGPA <=4.0:
        print("Your Grade is A ")
    elif CGPA >= 3.3 and CGPA <= 3.69:
        print("Your Grade is B+")
    elif CGPA >=3.0 and CGPA <= 3.29:
        print("Your Grade is B")
    elif CGPA >= 2.5 and CGPA <= 2.99:
        print("Your Grade is C+")
    elif CGPA >= 2.0 and CGPA <= 2.49:
        print("Your Grade is C")
    elif CGPA >= 1.5 and CGPA <= 1.99:
        print("Your Grade is D")
    else:
        print("Your Grade is F")
        

if Semester != 1:
    Prev_SemcGPA = float(input(f"Enter the CGPA of Previous Semesters: "))
    Prev_SemCH = int(input("Enter the Previous Credit Hours: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Prev_Points = Prev_SemcGPA * Prev_SemCH
    Curr_Points = TotalGPA * Total_credits
    Total_Points = Prev_Points + Curr_Points
    Total_CreditHours = Prev_SemCH + Total_credits
    
    New_CGPA = Total_Points/Total_CreditHours
    print(f"Your CGPA is: {New_CGPA}")
    Grade(New_CGPA)
else:
    print(f"Your CGPA is: {TotalGPA}")
    Grade(TotalGPA)    

