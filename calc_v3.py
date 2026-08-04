def start_calc():
  while True:
   try:
     user_input=input("Enter calculation : ")
     if user_input.lower()=="exit":
        print("Bye")
        break
     user_input=clean(user_input)
     user_input=user_input.split()
     new_tokens=[]
     new_tokens=pass1(user_input,new_tokens)
     if new_tokens== "ERROR":
      continue
     grand_total=float(new_tokens[0])
     grand_total=pass2(grand_total,new_tokens)
     print(grand_total)
   except:
     print("Invalid value or operation")


def clean(user_input):
    user_input=user_input.replace("+"," + ")
    user_input=user_input.replace("-"," - ")
    user_input=user_input.replace("*"," * ")
    user_input=user_input.replace("×"," * ")
    user_input=user_input.replace("/"," / ")
    user_input=user_input.replace("÷"," / ")

    return user_input
def pass1(user_input,new_tokens):
 i=0
 while i<len(user_input):
     if "*" in user_input[i] or "/" in user_input[i]:
        current_op=user_input[i]
        left_number=float(new_tokens.pop())
        right_number=float(user_input[i+1])
        i = i + 2
        if current_op=="*":
            total=left_number*right_number
            new_tokens.append(str(total))
        elif current_op=="/":
            if right_number==0 :
             print("Error,Dividing By Zero Is Not Allowed")
             return "ERROR"
            total1=left_number/right_number
            new_tokens.append(str(total1))
     else :
        new_tokens.append(user_input[i]) 
        i=i+1
 return new_tokens
def pass2(grand_total,new_tokens):
 for i in range(1,len(new_tokens),2):
    current_op2=new_tokens[i]
    if current_op2=="+":
        current_num=float(new_tokens[i+1])
        grand_total=grand_total+current_num
    elif current_op2=="-":
            current_num=float(new_tokens[i+1])
            grand_total=grand_total-current_num
 return grand_total

start_calc()



