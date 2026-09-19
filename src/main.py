import flet as ft
from app_state import AppState
from home import Home
from profile import Profile

# 전역 상태 인스턴스 생성
global_state = AppState()



# App 최상위 컴포넌트도 state를 받습니다.
@ft.component
def App(state: AppState):
    return ft.SafeArea(
        content=ft.Column(
            [
              
                ft.Router(
                    [
                        ft.Route(index=True, component=lambda: Home(state=state)),
                        ft.Route(index="profile", component=lambda: Home(state=state)),
                    ]
                ),
            ]
        )
    )

@ft.component
def MainApp():
    # 여기서 App에 상태를 주입합니다.
    return App(state=global_state)

# 👇 새롭게 추가된 일반 main 함수
def main(page: ft.Page):
    page.title = "MyWeek"
    page.appbar = ft.AppBar(
        title=ft.Text("My Week"),
        bgcolor="#ffbb00",
        actions=[ft.IconButton(ft.Icons.HOME, on_click=lambda e: ft.context.page.navigate("/")), ft.IconButton(ft.Icons.PERSON_2_OUTLINED, on_click=lambda e: ft.context.page.navigate("/profile")), ft.IconButton(ft.Icons.SHOPPING_CART,  on_click=lambda e: ft.context.page.navigate("/cart")), ft.IconButton(ft.Icons.PAYMENT,on_click=lambda e: ft.context.page.navigate("/pay"))],
        )
    page.render(MainApp) 


if __name__ == "__main__":
    ft.run(main)

