import tkinter
from tkinter import *

root=Tk()
root.title("GPA Calculator")
root.geometry("520x560")

def main():
    # get grade points from entry
    grade_1st=str(grade1_entry.get().strip())
    grade_2nd=str(grade2_entry.get().strip())
    grade_3rd=str(grade3_entry.get().strip())
    grade_4th=str(grade4_entry.get().strip())
    grade_5th=str(grade5_entry.get().strip())
    grade_6th=str(grade6_entry.get().strip())

    # get credits from entry
    credit_1=int(credit1_entry.get())
    credit_2=int(credit2_entry.get())
    credit_3=int(credit3_entry.get())
    credit_4=int(credit4_entry.get())
    credit_5=int(credit5_entry.get())
    credit_6=int(credit6_entry.get())

    # call funtions
    total_GP = add_grade_points(grade_1st, grade_2nd,grade_3rd,grade_4th,grade_5th,grade_6th, credit_1, credit_2, credit_3, credit_4, credit_5, credit_6)
    total_credits = add_credits(credit_1,credit_2,credit_3,credit_4,credit_5,credit_6)
    GPA = compute_GPA(total_GP,total_credits)
    compute_percentile(GPA)

def add_grade_points(grade_1st, grade_2nd,grade_3rd,grade_4th,grade_5th,grade_6th, credit_1, credit_2, credit_3, credit_4, credit_5, credit_6):
    # Letter Grade convertion to numbers
    grades = [4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
    
    # compute letter grade into float
    def compute_grade_1():

        if grade_1st == "A":
            grade_point1 = float(grades[0])
        elif grade_1st == "A-":
            grade_point1 = float(grades[1])
        elif grade_1st == "B+":
            grade_point1 = float(grades[2])
        elif grade_1st == "B":
            grade_point1 = float(grades[3])
        elif grade_1st == "B-":
            grade_point1 = float(grades[4])
        elif grade_1st == "C+":
            grade_point1 = float(grades[5])
        elif grade_1st == "C":
            grade_point1 = float(grades[6])
        elif grade_1st == "C-":
            grade_point1 = float(grades[7])
        elif grade_1st == "D+":
            grade_point1 = float(grades[8])
        elif grade_1st == "D":
            grade_point1 = float(grades[9])
        elif grade_1st == "F":
            grade_point1 = float(grades[10])
        else:
            Label(text="Error (unvalid letter)",font="arial 12 bold").place(x=250,y=320)

        return grade_point1

    def compute_grade_2():

        if grade_2nd == "A":
            grade_point2 = float(grades[0])
        elif grade_2nd == "A-":
            grade_point2 = float(grades[1])
        elif grade_2nd == "B+":
            grade_point2 = float(grades[2])
        elif grade_2nd == "B":
            grade_point2 = float(grades[3])
        elif grade_2nd == "B-":
            grade_point2 = float(grades[4])
        elif grade_2nd == "C+":
            grade_point2 = float(grades[5])
        elif grade_2nd == "C":
            grade_point2 = float(grades[6])
        elif grade_2nd == "C-":
            grade_point2 = float(grades[7])
        elif grade_2nd == "D+":
            grade_point2 = float(grades[8])
        elif grade_2nd == "D":
            grade_point2 = float(grades[9])
        elif grade_2nd == "F":
            grade_point2 = float(grades[10])
        else:
            Label(text="Error",font="arial 12 bold").place(x=250,y=320)
        
        return grade_point2

    def compute_grade_3():

        if grade_3rd == "A":
            grade_point3 = float(grades[0])
        elif grade_3rd == "A-":
            grade_point3 = float(grades[1])
        elif grade_3rd == "B+":
            grade_point3 = float(grades[2])
        elif grade_3rd == "B":
            grade_point3 = float(grades[3])
        elif grade_3rd == "B-":
            grade_point3 = float(grades[4])
        elif grade_3rd == "C+":
            grade_point3 = float(grades[5])
        elif grade_3rd == "C":
            grade_point3 = float(grades[6])
        elif grade_3rd == "C-":
            grade_point3 = float(grades[7])
        elif grade_3rd == "D+":
            grade_point3 = float(grades[8])
        elif grade_3rd == "D":
            grade_point3 = float(grades[9])
        elif grade_3rd == "F":
            grade_point3 = float(grades[10])
        else:
            Label(text="Error",font="arial 12 bold").place(x=250,y=320)
        
        return grade_point3

    def compute_grade_4():

        if grade_4th == "A":
            grade_point4 = float(grades[0])
        elif grade_4th == "A-":
            grade_point4 = float(grades[1])
        elif grade_4th == "B+":
            grade_point4 = float(grades[2])
        elif grade_4th == "B":
            grade_point4 = float(grades[3])
        elif grade_4th == "B-":
            grade_point4 = float(grades[4])
        elif grade_4th == "C+":
            grade_point4 = float(grades[5])
        elif grade_4th == "C":
            grade_point4 = float(grades[6])
        elif grade_4th == "C-":
            grade_point4 = float(grades[7])
        elif grade_4th == "D+":
            grade_point4 = float(grades[8])
        elif grade_4th == "D":
            grade_point4 = float(grades[9])
        elif grade_4th == "F":
            grade_point4 = float(grades[10])
        else:
            Label(text="Error",font="arial 12 bold").place(x=250,y=320)
        
        return grade_point4

    def compute_grade_5():

        if grade_5th == "A":
            grade_point5 = float(grades[0])
        elif grade_5th == "A-":
            grade_point5 = float(grades[1])
        elif grade_5th == "B+":
            grade_point5 = float(grades[2])
        elif grade_5th == "B":
            grade_point5 = float(grades[3])
        elif grade_5th == "B-":
            grade_point5 = float(grades[4])
        elif grade_5th == "C+":
            grade_point5 = float(grades[5])
        elif grade_5th == "C":
            grade_point5 = float(grades[6])
        elif grade_5th == "C-":
            grade_point5 = float(grades[7])
        elif grade_5th == "D+":
            grade_point5 = float(grades[8])
        elif grade_5th == "D":
            grade_point5 = float(grades[9])
        elif grade_5th == "F":
            grade_point5 = float(grades[10])
        else:
            Label(text="Error",font="arial 12 bold").place(x=250,y=320)
        
        return grade_point5

    def compute_grade_6():

        if grade_6th == "A":
            grade_point6 = float(grades[0])
        elif grade_6th == "A-":
            grade_point6 = float(grades[1])
        elif grade_6th == "B+":
            grade_point6 = float(grades[2])
        elif grade_6th == "B":
            grade_point6 = float(grades[3])
        elif grade_6th == "B-":
            grade_point6 = float(grades[4])
        elif grade_6th == "C+":
            grade_point6 = float(grades[5])
        elif grade_6th == "C":
            grade_point6 = float(grades[6])
        elif grade_6th == "C-":
            grade_point6 = float(grades[7])
        elif grade_6th == "D+":
            grade_point6 = float(grades[8])
        elif grade_6th == "D":
            grade_point6 = float(grades[9])
        elif grade_6th == "F":
            grade_point6 = float(grades[10])
        else:
            Label(text="Error",font="arial 12 bold").place(x=250,y=320)
        
        return grade_point6

    grade_1 = compute_grade_1()
    grade_2 = compute_grade_2()
    grade_3 = compute_grade_3()
    grade_4 = compute_grade_4()
    grade_5 = compute_grade_5()
    grade_6 = compute_grade_6()
    
    # Total Grade Points based on credits
    def compute_total_points():

        grade_point_1 = grade_1 * credit_1
        grade_point_2 = grade_2 * credit_2
        grade_point_3 = grade_3 * credit_3
        grade_point_4 = grade_4 * credit_4
        grade_point_5 = grade_5 * credit_5
        grade_point_6 = grade_6 * credit_6

        total_points = (grade_point_1 + grade_point_2 + grade_point_3 + grade_point_4 + grade_point_5 + grade_point_6)
        Label(text=f"{total_points:.1f}                                    ",font="arial 12 bold").place(x=250,y=320)

        return round(total_points , 1)

    total_points = (compute_total_points())

    return total_points

def add_credits(credit_1,credit_2,credit_3,credit_4,credit_5,credit_6):


    total_credits=(credit_1 + credit_2 + credit_3 + credit_4 + credit_5 + credit_6)
    Label(text=f"{total_credits}                        ",font="arial 12 bold").place(x=250,y=350)

    return int(total_credits)

def compute_GPA(Grade_Points, Credits):
    GPA = (Grade_Points / int(Credits))
    Label(text=f"{GPA:.2f}     ",font="arial 12 bold").place(x=250,y=380)

    return float(round(GPA, 2))

def compute_percentile(GPA):

    grade_pa = GPA

    if grade_pa== 4:
        percent = "95th percentile"
    elif grade_pa >= 3.5:
        percent = "90th percentile"
    elif grade_pa >= 3:
        percent = "85th percentile"
    elif grade_pa >= 2.5:
        percent = "80th percentile"
    elif grade_pa >= 2:
        percent = "75th percentile"
    elif grade_pa >= 1.5:
        percent = "70th percentile"
    elif grade_pa >= 1:
        percent = "65th percentile"
    else:
        percent = "Below 65th percentile"



    Label(text=f"{percent}                        ",font="arial 12 bold").place(x=250,y=410)
    return percent

# title
title=Label(root,text="Grade Point Average", font="arial 18")
title.place(x=150,y=10)
title2=Label(root,text="Calculator", font="arial 18")
title2.place(x=200,y=40)

# catergory sub_titles
classes=Label(root,text="Classes", font="arial 14")
classes.place(x=80,y=80)
Letter_grade=Label(root,text="Letter grades", font="arial 14")
Letter_grade.place(x=200,y=80)
credits=Label(root,text="Credits", font="arial 14")
credits.place(x=360,y=80)

# results
grade_tot=Label(root,text="Total Grade Points:", font="arial 12")
credits_tot=Label(root,text="Total Credits:", font="arial 12")
gpa=Label(root,text="GPA:", font="arial 12")
percentile=Label(root,text="Percentile:", font="arial 12")

# cordinates for results
grade_tot.place(x=50,y=320)
credits_tot.place(x=50,y=350)
gpa.place(x=50,y=380)
percentile.place(x=50,y=410)

# classes entry
sub1=Entry(root,font="arial 12",width=15)
sub2=Entry(root,font="arial 12",width=15)
sub3=Entry(root,font="arial 12",width=15)
sub4=Entry(root,font="arial 12",width=15)
sub5=Entry(root,font="arial 12",width=15)
sub6=Entry(root,font="arial 12",width=15)

# cordinates for Classes
sub1.place(x=50,y=120)
sub2.place(x=50,y=150)
sub3.place(x=50,y=180)
sub4.place(x=50,y=210)
sub5.place(x=50,y=240)
sub6.place(x=50,y=270)
    
# Takes grade value from entry
grade1value=StringVar(value="F")
grade2value=StringVar(value="F")
grade3value=StringVar(value="F")
grade4value=StringVar(value="F")
grade5value=StringVar(value="F")
grade6value=StringVar(value="F")

grade1_entry=Entry(root,textvariable=grade1value,font="arial 12",width=2)
grade2_entry=Entry(root,textvariable=grade2value,font="arial 12",width=2)
grade3_entry=Entry(root,textvariable=grade3value,font="arial 12",width=2)
grade4_entry=Entry(root,textvariable=grade4value,font="arial 12",width=2)
grade5_entry=Entry(root,textvariable=grade5value,font="arial 12",width=2)
grade6_entry=Entry(root,textvariable=grade6value,font="arial 12",width=2)

# Letter Grade entry cordinates
grade1_entry.place(x=250,y=120)
grade2_entry.place(x=250,y=150)
grade3_entry.place(x=250,y=180)
grade4_entry.place(x=250,y=210)
grade5_entry.place(x=250,y=240)
grade6_entry.place(x=250,y=270)

# Takes credits value from entry
credit1value=IntVar()
credit2value=IntVar()
credit3value=IntVar()
credit4value=IntVar()
credit5value=IntVar()
credit6value=IntVar()

credit1_entry=Entry(root,textvariable=credit1value,font="arial 12",width=1)
credit2_entry=Entry(root,textvariable=credit2value,font="arial 12",width=1)
credit3_entry=Entry(root,textvariable=credit3value,font="arial 12",width=1)
credit4_entry=Entry(root,textvariable=credit4value,font="arial 12",width=1)
credit5_entry=Entry(root,textvariable=credit5value,font="arial 12",width=1)
credit6_entry=Entry(root,textvariable=credit6value,font="arial 12",width=1)

# credit entry cordinates
credit1_entry.place(x=390,y=120)
credit2_entry.place(x=390,y=150)
credit3_entry.place(x=390,y=180)
credit4_entry.place(x=390,y=210)
credit5_entry.place(x=390,y=240)
credit6_entry.place(x=390,y=270)

# buttons Attributes
Button(text="Calculate", font="arial 15", bg="white",bd=10,width=8,command=main).place(x=50,y=480)
Button(text="Exit", font="arial 15",bg="white",bd=10,width=8,command=lambda:exit()).place(x=350,y=480)

root.mainloop()