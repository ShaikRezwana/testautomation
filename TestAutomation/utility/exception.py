
try:
    user_input1=input("please enter first number")
    user_input2=input("please enter second number")
    c=int(user_input1)+int(user_input2)
    print(c)
except:
    print("your input is incorrect, please enter valid input")
finally:
    print("this code i want to execute at the end")
