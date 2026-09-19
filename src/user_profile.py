import flet as ft
from app_state import AppState

@ft.component
def Profile(state: AppState):
    return ft.Column(
            controls=[
                ft.Text("Profile!", size=50),
            ]
        )