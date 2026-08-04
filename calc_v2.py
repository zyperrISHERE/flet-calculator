print("Intermediate calculator by Zyperr")
def add(calc_input):
    calc_input=calc_input.split("+")
    num1,num2=float(calc_input[0]),float(calc_input[1])
    return num1+num2
def subtract(calc_input):
    calc_input=calc_input.split("-")
    num1,num2=float(calc_input[0]),float(calc_input[1])
    return num1-num2
def multiply(calc_input):
    calc_input=calc_input.split("*")
    num1,num2=float(calc_input[0]),float(calc_input[1])
    return num1*num2
def divide(calc_input): 
    calc_input=calc_input.split("/")
    num1,num2=float(calc_input[0]),float(calc_input[1])
    if num2==0:
        return "Dividing By Zero Is Not allowed"
    return num1/num2
def clean(calc_input):
    calc_input=calc_input.replace(" ","")
    calc_input=calc_input.replace("x","*")
    calc_input=calc_input.replace("X","*")
    calc_input=calc_input.replace("×","*")
    calc_input=calc_input.replace("÷","/")
    return calc_input
    

while True:
    calc_input=input("Enter Your Calculation, e.g like (8÷8) : " )
    if calc_input.lower()=="exit":
          print("Goodbye! Thanks for using Zyperr's calculator.")
          break
    calc_input=clean(calc_input)
    try:
       if "+" in calc_input:
        print(add(calc_input))
       elif "-" in calc_input:
        print(subtract(calc_input))
       elif  "*" in calc_input:
        print(multiply(calc_input))
       elif "/" in calc_input:
        print(divide(calc_input))
       else:
        print(" Error: No valid operator found (+, -, *, /).")
    except:
     print("Invalid expression! Please enter a valid format (e.g., 5+5).")
