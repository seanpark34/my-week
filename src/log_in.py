import flet as ft
from app_state import AppState
from flet import CupertinoIcons


def _register_user(state: AppState, username: str, password: str, confirmation: str) -> str | None:
    if not username or not password:
        return "아이디와 비밀번호를 입력해 주세요."
    if len(password) < 8:
        return "비밀번호는 8자 이상 입력해 주세요."
    if password != confirmation:
        return "비밀번호가 서로 일치하지 않습니다."
    if any(user["id"].casefold() == username.casefold() for user in state.users):
        return "이미 사용 중인 아이디입니다."

    state.add_user({"id": username, "password": password})
    state.set_logged_in({"id": username})
    return None


async def _authenticate_user(state: AppState, username: str, password: str) -> str | None:
    if not username or not password:
        return "아이디와 비밀번호를 입력해 주세요."

    user = next(
        (
            account for account in state.users
            if account["id"].casefold() == username.casefold()
            and account["password"] == password
        ),
        None,
    )
    if user is None:
        return "아이디 또는 비밀번호가 올바르지 않습니다."

    state.users = [user, *(account for account in state.users if account is not user)]
    state.set_logged_in(user)
    await state.load_user_data()
    return None


@ft.component
def LogIn(state: AppState, page: ft.Page):
    is_signup, set_is_signup = ft.use_state(False)
    username_value, set_username_value = ft.use_state("")
    password, set_password = ft.use_state(True)
    password_value, set_password_value = ft.use_state("")
    confirm_password_value, set_confirm_password_value = ft.use_state("")
    error_message, set_error_message = ft.use_state("")

    async def handle_login(_):
        username = username_value.strip()
        if is_signup:
            error = _register_user(
                state, username, password_value, confirm_password_value
            )
        else:
            error = await _authenticate_user(state, username, password_value)

        if error:
            set_error_message(error)
            return
        set_error_message("")
        page.navigate("/calendar")

    def toggle_password(_):
        set_password(not password)

    def toggle_mode(_):
        set_is_signup(not is_signup)
        set_password_value("")
        set_confirm_password_value("")
        set_error_message("")

    def update_username(e):
        set_username_value(e.control.value or "")
        set_error_message("")

    def update_password(e):
        set_password_value(e.control.value or "")
        set_error_message("")

    def update_confirm_password(e):
        set_confirm_password_value(e.control.value or "")
        set_error_message("")

    icon = CupertinoIcons.EYE_SLASH if password else CupertinoIcons.EYE
    title = "회원가입" if is_signup else "로그인"

    return ft.Column(
        controls=[
            ft.Text("MyWeek", size=18, color="#52616B"),
            ft.Text(title, size=40),
            ft.Text(
                "새 계정을 만들어 일주일 계획을 관리하세요."
                if is_signup else "계정에 로그인해 계획을 이어가세요.",
                color="#52616B",
            ),
            ft.TextField(
                label="아이디",
                value=username_value,
                on_change=update_username,
            ),
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon,
                        on_click=toggle_password,
                        tooltip="비밀번호 표시 전환",
                    ),
                    ft.TextField(
                        label="비밀번호",
                        value=password_value,
                        password=password,
                        on_change=update_password,
                    ),
                ]
            ),
            ft.TextField(
                label="비밀번호 확인",
                value=confirm_password_value,
                password=password,
                on_change=update_confirm_password,
            ) if is_signup else ft.Container(),
            ft.Text(error_message, color="#B42318") if error_message else ft.Container(),
            ft.Button(
                "가입하기" if is_signup else "로그인",
                on_click=handle_login,
                bgcolor="#60FA41",
            ),
            ft.Button(
                "이미 계정이 있어요. 로그인" if is_signup else "계정이 없으신가요? 회원가입",
                on_click=toggle_mode,
            ),
        ]
    )