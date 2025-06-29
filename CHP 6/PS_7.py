# Write a program to find out whether a given post is talking about “python” or not.

post = input("Enter your post: ")

if "python" in post.lower():
    print("The post is talking about python")
else:
    print("The post is not talking about python")