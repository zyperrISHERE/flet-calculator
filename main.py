import flet as ft
def main(page:ft.Page):
    page.window_width=360
    page.window_height=540
    page.window.resizable = False
    page.theme_mode=ft.ThemeMode.DARK
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    displayscreen=ft.TextField(
        value="",
        width=280,
        read_only=True,
        text_align="right",
        color="black",
        bgcolor="white",
        text_size=42,
        border_radius=50,
        border_color="red"
    )
    def clean(user_input):
     user_input=user_input.replace("+"," + ")
     user_input=user_input.replace("-"," - ")
     user_input=user_input.replace("**","@Power@")
     user_input=user_input.replace("*"," * ")
     user_input=user_input.replace("@Power@"," ** ")
     user_input=user_input.replace("ร—"," * ")
     user_input=user_input.replace("/"," / ")
     user_input=user_input.replace("รท"," / ")

     return user_input
    def pass1(user_input,new_tokens):
     i=0
     while i<len(user_input):
         if "*" == user_input[i] or "/" == user_input[i] or "**" == user_input[i]:
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
             elif current_op=="**":
                 total2=left_number**right_number
                 new_tokens.append(str(total2))
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
    

    def btn_click(e):
        char = e.control.content.value
        screen=displayscreen.value
        if char=="C":
            displayscreen.value=""
        elif char=="=":
            try:
             screen=clean(displayscreen.value)
             tokens=screen.split()
             new_tokens=pass1(tokens,[])
             if new_tokens=="ERROR":
                displayscreen.value="Error"
             else:
              grand_total=float(new_tokens[0])
              grand_total=pass2(grand_total,new_tokens)
              if int(grand_total)==grand_total:
                 grand_total=int(grand_total)
             displayscreen.value=str(grand_total)
            except:
              displayscreen.value="Error"
        else:
            if displayscreen.value=="Error":
             displayscreen.value=""
            displayscreen.value+=char
        page.update()
    row1=ft.Row(
        controls=[
           ft.Button(content=ft.Text("7", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
           ft.Button(content=ft.Text("8", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
           ft.Button(content=ft.Text("9", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
          ft.Button(content=ft.Text("/", color="white", size=20, weight="bold"), bgcolor="orange", width=60, height=60, on_click=btn_click),
           ft.Button(content=ft.Text("**", color="white", size=20, weight="bold"), bgcolor="orange", width=70, height=60, on_click=btn_click)
         ],
         alignment=ft.MainAxisAlignment.CENTER,
         spacing=10
    )
    row2=ft.Row(
            controls=[
              ft.Button(content=ft.Text("4", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
               ft.Button(content=ft.Text("5", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
              ft.Button(content=ft.Text("6", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
              ft.Button(content=ft.Text("*", color="white", size=20, weight="bold"),bgcolor="orange",width=70, height=60,on_click=btn_click)
             ],
             alignment=ft.MainAxisAlignment.CENTER,
             spacing=10
        )
    row3=ft.Row(
                controls=[
                  ft.Button(content=ft.Text("1", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                   ft.Button(content=ft.Text("2", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                   ft.Button(content=ft.Text("3", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                  ft.Button(content=ft.Text("-", color="white", size=20, weight="bold"),bgcolor="orange",width=70, height=60,on_click=btn_click)
                 ],
                 alignment=ft.MainAxisAlignment.CENTER,
                 spacing=10
            )
    row4=ft.Row(
                    controls=[
                      ft.Button(content=ft.Text("C", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                       ft.Button(content=ft.Text("0", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                       ft.Button(content=ft.Text("+", color="white", size=20, weight="bold"),width=70,bgcolor="orange" ,height=60,on_click=btn_click),
                       ft.Button(content=ft.Text("=", color="white", size=20, weight="bold"),bgcolor="green",width=70, height=60,on_click=btn_click)
                     ],
                     alignment=ft.MainAxisAlignment.CENTER,
                     spacing=10
                )
    page.add(
    ft.Container(
        width=400,
        padding=20,
        border_radius=25,
        bgcolor="#1E1E2C",
        content=ft.Column(
            controls=[
                displayscreen,
                row1,
                row2,
                row3,
                row4
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
)
ft.run(main)

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
    

    def btn_click(e):
        char = e.control.content.value
        screen=displayscreen.value
        if char=="C":
            displayscreen.value=""
        elif char=="=":
            try:
             screen=clean(displayscreen.value)
             tokens=screen.split()
             new_tokens=pass1(tokens,[])
             if new_tokens=="ERROR":
                displayscreen.value="Error"
             else:
              grand_total=float(new_tokens[0])
              grand_total=pass2(grand_total,new_tokens)
              displayscreen.value=str(grand_total)
            except:
              displayscreen.value="Error"
        else:
            if displayscreen.value=="Error":
             displayscreen.value=""
            displayscreen.value+=char
        page.update()
    row1=ft.Row(
        controls=[
           ft.Button(content=ft.Text("7", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
           ft.Button(content=ft.Text("8", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
           ft.Button(content=ft.Text("9", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
          ft.Button(content=ft.Text("/", color="white", size=20, weight="bold"), bgcolor="orange", width=60, height=60, on_click=btn_click),
         ],
         alignment=ft.MainAxisAlignment.CENTER,
         spacing=10
    )
    row2=ft.Row(
            controls=[
              ft.Button(content=ft.Text("4", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
               ft.Button(content=ft.Text("5", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
              ft.Button(content=ft.Text("6", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
              ft.Button(content=ft.Text("*", color="white", size=20, weight="bold"),bgcolor="orange",width=70, height=60,on_click=btn_click)
             ],
             alignment=ft.MainAxisAlignment.CENTER,
             spacing=10
        )
    row3=ft.Row(
                controls=[
                  ft.Button(content=ft.Text("1", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                   ft.Button(content=ft.Text("2", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                   ft.Button(content=ft.Text("3", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                  ft.Button(content=ft.Text("-", color="white", size=20, weight="bold"),bgcolor="orange",width=70, height=60,on_click=btn_click)
                 ],
                 alignment=ft.MainAxisAlignment.CENTER,
                 spacing=10
            )
    row4=ft.Row(
                    controls=[
                      ft.Button(content=ft.Text("C", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                       ft.Button(content=ft.Text("0", color="white", size=20, weight="bold"),width=70, height=60,on_click=btn_click),
                       ft.Button(content=ft.Text("+", color="white", size=20, weight="bold"),width=70,bgcolor="orange" ,height=60,on_click=btn_click),
                       ft.Button(content=ft.Text("=", color="white", size=20, weight="bold"),bgcolor="green",width=70, height=60,on_click=btn_click)
                     ],
                     alignment=ft.MainAxisAlignment.CENTER,
                     spacing=10
                )
    page.add(
    ft.Container(
        width=340,
        padding=20,
        border_radius=25,
        bgcolor="#1E1E2C",
        content=ft.Column(
            controls=[
                displayscreen,
                row1,
                row2,
                row3,
                row4
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
)
ft.run(main)

