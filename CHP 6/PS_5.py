# Write a program which finds out whether a given name is present in a list or not

names = ["zidaan","eshaan","usaid","ayaan",]

search_name = input("Enter your name to search: ")

if (search_name in names):
    print("The name is in the list")
else:
    print("The name is not in the list")