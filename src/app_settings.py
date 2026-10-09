import flet as ft
from app_state import AppState

@ft.component
def Settings(state: AppState, page: ft.Page):
    if not state.is_logged_in:
        return ft.Column(
            controls=[
                ft.Text("로그인이 필요합니다.", size=30),
                ft.Button("로그인", on_click=lambda e: page.navigate("/log_in"), bgcolor="#60FA41"),
            ]
        )

    show_nickname_input, set_show_nickname_input = ft.use_state(False)
    nickname, set_nickname = ft.use_state(state.nickname)

    def update_nickname(e):
        set_nickname(e.control.value or "")

    def save_nickname(_):
        new_nickname = nickname.strip()
        if new_nickname:
            state.save_nickname(new_nickname)
            page.show_dialog(ft.SnackBar(ft.Text(f"닉네임이 저장되었습니다: {new_nickname}")))
        page.navigate("/profile")

    def log_out(_):
        state.login_done = 0
        page.navigate("/log_in")

    return ft.Column(
            controls=[
                ft.Text("설정", size=50),
                ft.Button(
                    "닉네임 변경",
                    on_click=lambda _: set_show_nickname_input(True),
                ),
                ft.TextField(
                    label="새 닉네임",
                    value=nickname,
                    on_change=update_nickname,
                ) if show_nickname_input else ft.Container(),
                ft.Button(
                    "저장", on_click=save_nickname, bgcolor="#60FA41"
                ) if show_nickname_input else ft.Container(),
                ft.Button(
                    "로그아웃", on_click=log_out, bgcolor="#FA4141"
                ),
            ]
        )
    