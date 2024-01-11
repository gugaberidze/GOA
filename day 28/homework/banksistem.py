

print("Hello this is GOA's bank" )
name = input("what's your name?")
lastname = input("what's your last name")
print("nice to meet you ")
print("create accaount")
email = input("enter your email")
password = input("enter password ")
confirm_password = input("enter your password if you want strong ")
deposit = int(input("enter money how much you want deposit "))
withdraw = int(input("enter money how much you wany withdraw"))
  
 
if password  == confirm_password:
    print("your password is right")

else:
    print("this password is not right")


if deposit < withdraw:
    print("you have not money in your bank accaount")

else:
    print("congrulations you have money in your bank accaunt")


