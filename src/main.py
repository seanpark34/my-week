import flet as ft
from app_state import AppState
from home_view import Home
from user_profile import Profile
from calendar_view import Calendar
from app_settings import Settings
from add_plan import Plans
from one_week_plan import Week_Plan
from plan_progress import progress
from log_in import LogIn

@ft.component
def App(state: AppState, page: ft.Page):
    return ft.SafeArea(
        content=ft.Column(
            [
              
                ft.Router(
                    [
                        ft.Route(index=True, component=lambda: Home(state=state, page=page)),
                        ft.Route(path="/profile", component=lambda: Profile(state=state, page=page)),
                        ft.Route(path="/calendar", component=lambda: Calendar(state=state, page=page)),
                        ft.Route(path="/settings", component=lambda: Settings(state=state, page=page)),
                        ft.Route(
                            path="/add_plan/:week_key", 
                            component=lambda: Plans(state=state, page=page),
                        ),
                        ft.Route(path="/week_plan/:week_key", component=lambda: Week_Plan(state=state, page=page)),
                        ft.Route(path="/progress/:week_key/:plan_num", component=lambda: progress(state=state, page=page)),
                        ft.Route(path="/log_in", component=lambda: LogIn(state=state, page=page))
                    ]
                )
            ]
        )
    )

@ft.component
def MainApp(state: AppState, page: ft.Page):
    return App(state=state, page=page)

appbar_text="My Week"

async def main(page: ft.Page):
    prefs = ft.SharedPreferences()
    global_state = AppState(prefs=prefs, page=page)
    await global_state.load_state_async()
    # page.on_route_change = global_state.save_user_data

    page.title = "MyWeek"
    page.appbar = ft.AppBar(
        title=ft.Text(appbar_text),
        bgcolor="#ffbb00",
        actions=[
            ft.IconButton(ft.Icons.PERSON_2_OUTLINED, on_click=lambda e: page.navigate("/profile")),
            ft.IconButton(ft.Icons.CALENDAR_MONTH, on_click=lambda e: page.navigate("/calendar")),
            ft.IconButton(ft.Icons.SETTINGS, on_click=lambda e: page.navigate("/settings")),
        ],
    )
    page.render(lambda: MainApp(state=global_state, page=page))

if __name__ == "__main__":
    ft.run(main)