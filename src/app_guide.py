import flet as ft
from app_state import AppState

@ft.component
def Guide(state: AppState, page: ft.Page):
    return ft.Column(
        controls=[
            ft.Text("📖앱 사용 가이드", size=30),
            ft.Text("", size = 20),
            ft.Text("안녕하세요! MyWeek를 사용해주셔서 감사합니다.", size=20),
            ft.Text("MyWeek는 쉽게 일주일 단위로 계획을 세우고 실천할 수 있게 도와주는 앱입니다.", size=20),
            ft.Text("", size = 20),
            ft.Text("일주일 단위로 계획을 세우면 좋은점이 많아요!", size=20),
            ft.Text("1. 시간이 정해저있지 않아 혼자서 시간을 잘 활용할 수 있어요!", size=20),
            ft.Text("2. 한 주 안에서 밀리면 다음날 더 열심히 할 수 있어요!", size=20),
            ft.Text("3. 반대로 한 주 안에서 빨리 할 일을 끝내면 놀 수 있어요!", size=20),
            ft.Text("4. 오늘 할 일을 잘 하지 못해도 내일이 있기 때문에 안심할 수 있어요!", size=20),
            ft.Text("5. 지난주에 무엇을 했는지 돌아보고 더 좋은 계획을 세울 수 있어요!", size=20),
            ft.Text("", size = 20),
            ft.Text("MyWeek에서 쉽게 계획을 세우고 실천해 한주씩 계획을 세우는 것의 공부 효과를 느껴보세요!", size=20),


 
        ]
    )