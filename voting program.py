#voting program
age = int(input("enter age"))
citizenship = input("enter citizenship")
if age >= 18 and citizenship in ["kenyan", "ugandan", "tanzanian"]:
    print(" you are eligible to vote")
else:
    print(" you are not eligible to vote")
    
