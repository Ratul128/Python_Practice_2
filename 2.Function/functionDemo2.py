#kl to mile------------------
def kl_to_mile(conv_rate):
    kilo=int(input("Enter Kl:"))
    result=conv_rate*kilo
    print("Kl to Mile:",result)

#taka to rupee---------------
def tk_To_Rupee(conv_rate):
    tk=int(input("Enter the amount(tk):"))
    result=conv_rate*tk
    print(f"Your Rupee is:{result}")

#Rupee to doller convert----------
def rupee_to_dollar(conv_rate):
    rupee=int(input("Enter the amount(rupee):"))
    result=conv_rate*rupee
    print(f"Your Doller is:{result}")

#Taka to doller convert----------
def tk_to_doller(conv_rate):
    tk=int(input("Enter the amount(tk):"))
    result=conv_rate*tk
    print(f"Your Doller is:{result}")


kl_to_mile(0.62)
tk_To_Rupee(0.78)
rupee_to_dollar(0.012)
tk_to_doller(0.0083)

