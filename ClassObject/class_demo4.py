
class Calculator:
    def summation(self,num1,num2):
        return num1+num2

    def subtract(self,num1,num2):
        return num1-num2

    def multiply(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        return num1/num2

if __name__ =='__main__':
    calculator_obj=Calculator()
    print(calculator_obj.summation(10,20))
    print(calculator_obj.subtract(50,10))
    print(calculator_obj.multiply(20,10))
    print(calculator_obj.divide(100,10))