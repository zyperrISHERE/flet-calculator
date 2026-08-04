import flet as ft
def main(page : ft.Page):
    page.theme_mode=ft.ThemeMode.DARK
    page.window_width=500
    page.window_height=450
    page.title="Score counter"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    score=0
    score_text=ft.Text(
        value=f"Score : {score}",
        size=32,
        weight="bold"
    )
    def plus_score(e):
        nonlocal score
        score+=1
        score_text.value=f"Score : {score}"
        page.update()
    def clear_score(e):
        nonlocal score
        score=0
        score_text.value=f"Score : {score}"
        page.update()
    def minus_score(e):
        nonlocal score
        score-=1
        score_text.value=f"Score : {score}"
        page.update()
    btn1=ft.ElevatedButton(
        content=ft.Text("-1"),
        bgcolor="red",
        on_click=minus_score

    )
    btn2=ft.ElevatedButton(
        content=ft.Text("Reset"),
        bgcolor="grey",
        on_click=clear_score

    )
    btn3=ft.ElevatedButton(
        content=ft.Text("+1"),
        bgcolor="green",
        on_click=plus_score
    )
    btn_row=ft.Row(
       controls=[btn1,btn2,btn3],
       spacing=15,
       alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(score_text,btn_row)
ft.run(main)