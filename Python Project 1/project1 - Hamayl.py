def is_applicable(cgpa):

    if cgpa > 3.5:
        print("You Are Applicable")
        return True
    else:
        print("NOT Applicable for this Scholarship")
        return False

def application():

    print("        Scholarship  Application         ")
    return None

def scholarship_award():

    high_cgpa = 0.0
    high_cgpa_student = " "

    for i in range(4):
        name = input(f"Enter Name of Student {i +1} :  ")
        cgpa = float(input(f"Enter CGPA of Student{i +1}:  "))

        if is_applicable(cgpa):
            if cgpa > high_cgpa:
                high_cgpa = cgpa
                high_cgpa_student = name

    if high_cgpa > 0:
        print(f"CONGRATULATIONS !! {high_cgpa_student} is awarded with Fully Funded Scholarship")
    else:
        print("No student is eligible.")

application()
scholarship_award()