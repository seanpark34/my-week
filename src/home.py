import flet as ft
from app_state import AppState

@ft.component
def Home(state: AppState):
    return ft.Column(
            controls=[
                ft.Text("Welcome to MyWeek!", size=50),
            ]
        )