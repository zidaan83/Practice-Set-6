# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = float(input("Enter marks for subject1: "))
sub2 = float(input("Enter marks for subject2: "))
sub3 = float(input("Enter marks for subject3: "))
sub4 = float(input("Enter marks for subject4: "))

total = sub1 + sub2 + sub3
percentage = (total/300)*100

if (percentage<=40 and sub1<=33 and sub2<=33 and sub3<=33):
    print("you are pass",percentage)
else:
    print("you failed")