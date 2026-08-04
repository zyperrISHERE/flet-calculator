def input1():
      num1=float(input("Enter first number : "))
      num2=float(input("Enter second number : "))
      return num1,num2




def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
          return "Cannot divide by zero"
        
    return a/b
 

def start_calc():
    print("Simple calculator yari by ZYPERR")
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 to exit")
    

    while True:
      choice=input("Enter your choice: ")
      if choice=="5":
              print("GO TO HELL")
              break
      elif choice=="1":
               num1,num2=input1()
               print(add(num1,num2))
      elif choice=="2":
              num1,num2=input1()
              print(subtract(num1,num2))
      elif choice=="3":
              num1,num2=input1()
              print(multiply(num1,num2))
      elif choice=="4":
              num1,num2=input1()
              print(division(num1,num2))
      else:
              print("Please enter a valid choice")







start_calc()
      



    















