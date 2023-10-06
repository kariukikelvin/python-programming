#grading system for three subjects
subject1 = int(input("enter subject1 marks"))
subject2 = int(input("enter subject2 marks"))
subject3 = int(input("enter subject3 marks"))
average = (subject1 + subject2 + subject3) * 1/3
if average >=70 and average <=100:
    print("A")
if average >=60 and average <70:
    print("B")
if average >=50 and average <60:
    print("C")
if average >=40 and average <50:
    print("D")
if average < 40:
    print("Fail")
