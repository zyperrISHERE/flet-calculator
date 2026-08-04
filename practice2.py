import flet as ft
def main(page : ft.Page):
    page.window_width=500
    page.window_height=450
    page.theme_mode=ft.ThemeMode.DARK
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    score1=ft.Text(
        value="Score : 0 ",
        size=28,
        weight=ft.FontWeight.BOLD
    )
    score=0
    def add_score(e):
            nonlocal score
            score+=1
            score1.value=f"Score : {score}"
            page.update()
    btn=ft.ElevatedButton(
        content=ft.Text("Score +1"),
        bgcolor="green",
        on_click=add_score
    )
    page.add(score1,btn)


ft.run(main)
                          