import flet as ft
def main(page: ft.Page):
    page.window_title_bar_hidden = True
    page.update()

if __name__ == "__main__":
    ft.app(main)

