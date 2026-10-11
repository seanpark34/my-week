import flet as ft
from app_state import AppState

@ft.component
def Home(state: AppState, page: ft.Page):
    return ft.Column(
            controls=[
                ft.Text("My Week에 오신 것을 환영합니다!", size=15),
                ft.Text("먼저 로그인을 해주세요.", size=25),
                ft.Button("로그인", on_click=lambda e: page.navigate("/log_in"), bgcolor="#60FA41"),
            ]
        )