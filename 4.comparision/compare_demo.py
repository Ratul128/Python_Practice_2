'''name="abc"
if name=="abc1":
    print("welcome")

else:
    print("Hlw")'''

def user_logIn(name,password):
    if name=="Ratul" and password=="1234":
        print("Logged in successfull")
    else:
        print("Logged in fail")

user_logIn(input("Enter Your Name:"),input("Enter Your Pass:"))