import flet as ft



def main(page: ft.Page):
    page.title = "Glassmorphism Demo"
    page.window_width = 430
    page.window_height = 700
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#10131C"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Background gradient
    background = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "#4F46E5",
                "#7C3AED",
                "#0EA5E9",
            ],
        ),
    )

    def glass_button(text, accent=False):
        return ft.Container(
            width=72,
            height=72,
            border_radius=22,
            bgcolor="#55FFFFFF" if not accent else "#55FF9800",
            border=ft.border.all(1, "#88FFFFFF"),
            shadow=ft.BoxShadow(
                blur_radius=18,
                spread_radius=0,
                color="#55000000",
                offset=ft.Offset(0, 6),
            ),
            alignment=ft.alignment.center,
            content=ft.Text(
                text,
                size=24,
                weight=ft.FontWeight.BOLD,
                color="white",
            ),
            ink=True,
        )

    display = ft.Container(
        height=90,
        border_radius=18,
        bgcolor="#33FFFFFF",
        border=ft.border.all(1, "#66FFFFFF"),
        padding=20,
        alignment=ft.alignment.center_right,
        content=ft.Text(
            "12,345",
            size=34,
            weight=ft.FontWeight.BOLD,
            color="white",
        ),
    )

    calculator = ft.Container(
        width=360,
        border_radius=32,
        bgcolor="#22FFFFFF",
        border=ft.border.all(1.5, "#66FFFFFF"),
        shadow=ft.BoxShadow(
            blur_radius=35,
            spread_radius=0,
            color="#66000000",
            offset=ft.Offset(0, 12),
        ),
        padding=20,
        content=ft.Column(
            tight=True,
            controls=[
                ft.Text(
                    "Glass Calculator",
                    size=18,
                    color="#DDFFFFFF",
                    weight=ft.FontWeight.W_500,
                ),
                ft.Divider(color="#22FFFFFF"),
                display,
                ft.Container(height=15),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        glass_button("7"),
                        glass_button("8"),
                        glass_button("9"),
                        glass_button("÷", True),
                    ],
                ),

                ft.Container(height=12),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        glass_button("4"),
                        glass_button("5"),
                        glass_button("6"),
                        glass_button("×", True),
                    ],
                ),

                ft.Container(height=12),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        glass_button("1"),
                        glass_button("2"),
                        glass_button("3"),
                        glass_button("-", True),
                    ],
                ),

                ft.Container(height=12),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        glass_button("C"),
                        glass_button("0"),
                        glass_button("."),
                        glass_button("+", True),
                    ],
                ),

                ft.Container(height=12),

                ft.Container(
                    height=65,
                    border_radius=22,
                    bgcolor="#66FFFFFF",
                    border=ft.border.all(1, "#AAFFFFFF"),
                    shadow=ft.BoxShadow(
                        blur_radius=20,
                        color="#44000000",
                        offset=ft.Offset(0, 5),
                    ),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "=",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                ),
            ],
        ),
    )

    page.add(
        ft.Stack(
            expand=True,
            controls=[
                background,
                ft.Container(
                    alignment=ft.alignment.center,
                    content=calculator,
                ),
            ],
        )
    )


ft.app(main)