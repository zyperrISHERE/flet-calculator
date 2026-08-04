import flet as ft
def main(page : ft.Page):
    page.window_height=450
    page.window_width=600
    page.title="Gaming Hub"
    page.theme_mode=ft.ThemeMode.DARK
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    text1=ft.Text(
        value="Select Your Target Page",
        size=20,
        weight=ft.FontWeight.BOLD

    )
    btn=ft.ElevatedButton(
        content=ft.Text("Launch Free Fire"),
        bgcolor="orange"
    )
    page.add(text1,btn)
    
ft.run(main)
