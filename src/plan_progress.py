import flet as ft
from app_state import AppState

@ft.component
def progress(state=AppState, page=ft.Page):
    week_key = ft.use_route_params().get("week_key")
    plan_num = int(ft.use_route_params().get("plan_num"))
    plans_of_the_week = state.plans_for_selected_week(week_key)

    chosen_plan = next(
        (
            plan
            for plan in plans_of_the_week
            if plan["num"] == plan_num
        ),
        None,
    )
    if chosen_plan is None:
        return ft.Text("선택한 계획을 찾을 수 없습니다.")

    done_count, set_done_count = ft.use_state(chosen_plan["Done"])

    def add_one_done():
        if done_count < chosen_plan["how_much"]:
            set_done_count(done_count + 1)
            chosen_plan["Done"] += 1
            state.save_plans()

    def remove_one_done():
        if done_count > 0:
            set_done_count(done_count - 1)
            chosen_plan["Done"] -= 1
            state.save_plans()

    def delete_this_plan(e):
        plans_of_the_week.remove(chosen_plan)
        state.save_plans()
        page.navigate(f"/week_plan/{week_key}")

    return ft.Column(
        controls=[
            ft.Text(f"{chosen_plan['name']} :", size=50),
            ft.Text(f"{chosen_plan['Done']}{chosen_plan['unit']}/{chosen_plan['how_much']}{chosen_plan['unit']} 완료", size=50),
            ft.Text(f"{done_count}/{chosen_plan['how_much']}", size=100),
            ft.Row(
                controls=[    
                    ft.IconButton(
                        ft.Icons.ADD_CIRCLE, on_click=add_one_done, icon_size=50),
                    ft.IconButton(
                        ft.Icons.REMOVE_CIRCLE, on_click=remove_one_done, icon_size=50),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Button("돌아가기", on_click=lambda e: page.navigate(f"/week_plan/{week_key}"), bgcolor="#60FA41"),
                    ft.Button("할 일 삭제", on_click=delete_this_plan, bgcolor="#FA4141"),
                ]
            )
        ]
    )

    