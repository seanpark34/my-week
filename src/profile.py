import flet as ft
from app_state import AppState

@ft.component
def Profile(state: AppState):
    return ft.Stack[
        ft.Image(src="icon.png", width=1200,),
    ]