import flet as ft
from app_state import AppState
from datetime import datetime, timedelta

@ft.component
def Week_Plan(state:AppState, page):
    week_key = ft.use_route_params().get("week_key")

    # today = datetime.now()
    # day_num = today.weekday()+1

    # if day_num == 7:
    #     day_num = 0
    # else:
    #     day_num = today.weekday()+1

    week_start = datetime.strptime(week_key, "%Y%m%d")
    # week_start = today + timedelta(-day_num + 7 * state.plan_week)
    week_start_m = week_start.strftime("%m")
    week_start_d = week_start.strftime("%d")
    week_end = week_start + timedelta(6)
    week_end_m = week_end.strftime("%m")
    week_end_d = week_end.strftime("%d")

    def plan_chosen(num):
        page.navigate(f"/progress/{week_key}/{num}")

    def check_button(plan):
        if plan["how_much"] <= plan["Done"]:
            return ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color="#60FA41")
        else:
            return ft.Icon(ft.Icons.CANCEL_ROUNDED, color="#FF0000")

    selected_week_plans = state.plans_for_selected_week(week_key)
    total_plan_types = len(selected_week_plans)
    completed_plan_types = sum(
        1
        for plan in selected_week_plans
        if plan.get("Done", 0) >= plan["how_much"]
    )
    progress_value = (
        completed_plan_types / total_plan_types if total_plan_types else 0
    )

    

    def go_to_add_plan():
        page.navigate(f"/add_plan/{week_key}")

    today = datetime.now()
    current_week_key = (today - timedelta(days=(today.weekday() + 1) % 7)).strftime("%Y%m%d")
    week_text = ft.Text(
        "지난주에 못한 것이 있다면 빨리 완료하세요!"
        if week_key < current_week_key
        else "계획을 세우고 실천하세요!",
        size=20,
    )

    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(str(week_start_m) + "/" + str(week_start_d) + "~" + str(week_end_m) + "/" + str(week_end_d), size=30),
                    (
                        ft.IconButton(ft.Icons.ADD_CIRCLE, on_click=lambda _: go_to_add_plan(), icon_size=30)
                        if week_key >= current_week_key 
                        else ft.Text("")
                    )
                ]
            ),
            week_text,
            ft.ProgressBar(value=progress_value, width=300, expand=1),
            *[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            ft.Icons.SEARCH_ROUNDED,
                            on_click=lambda _, num=plan["num"]: plan_chosen(num),
                        ),
                        ft.Text(f"{plan['name']} : {plan['Done']}{plan['unit']}/{plan['how_much']}{plan['unit']} 완료"),
                        check_button(plan),
                    ]
                )
                for plan in selected_week_plans
            ],
        ]
    )