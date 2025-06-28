# Write a program to find the greatest of four numbers entered by the user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

greatest = num1 

if num2>greatest:
    greatest = num2

elif num2>greatest:
    greatest = num3

elif num3>greatest:
    greatest = num4

print("The greatest number is: ",greatest)