import flet as ft
from app_state import AppState
from datetime import datetime, timedelta

@ft.component
def Plans(state: AppState, page: ft.Page):
    input_value, set_input_value = ft.use_state("")
    show_amount_input, set_show_amount_input = ft.use_state(False)
    selected_plan, set_selected_plan = ft.use_state("")
    amount_value, set_amount_value = ft.use_state("")
    unit_value, set_unit_value = ft.use_state("개")
    chosen_plan, set_chosen_plan = ft.use_state("")

    week_key = ft.use_route_params().get("week_key")
    
    def add_plan(_):
        plan = input_value.strip()
        if plan:
            set_input_value("")
            state.add_my_made_plan(plan)

    def update_input(e):
        set_input_value(e.control.value or "")

   
    def how_much_append(_):
        amount = amount_value.strip()
        unit = unit_value.strip()
        if selected_plan and amount.isdigit() and unit:
            existing_plan = next(
                (
                    plan
                    for plan in state.plans_for_selected_week(week_key)
                    if plan["name"] == selected_plan and plan["unit"] == unit
                ),
                None,
            )
            if existing_plan:
                existing_plan["how_much"] += int(amount)
            else:
                new_plan = {"name": selected_plan, "how_much": int(amount), "unit": unit, "Done": 0}
                state.add_plan_of_week(week_key, new_plan)
                # state.plans_for_selected_week(week_key).append({"num": state.list_num, "name": selected_plan, "how_much": int(amount), "unit": unit, "Done": 0})
                # state.list_num += 1
            set_amount_value("")
            page.navigate(f"/week_plan/{week_key}")

    def update_amount(e):
        set_amount_value(e.control.value or "")

    def update_unit(e):
        set_unit_value(e.control.value or "")

    def how_much():
        return ft.Row(
            controls=[
                ft.TextField(
                    label=chosen_plan+" : 수량(단위 빼고)",
                    value=amount_value,
                    expand=2,
                    on_change=update_amount,
                ),
                ft.TextField(
                    label="단위",
                    value=unit_value,
                    expand=1,
                    on_change=update_unit,
                ),
                ft.IconButton(
                    ft.Icons.SUBDIRECTORY_ARROW_LEFT_ROUNDED,
                    on_click=how_much_append,
                ),
            ]
        )
    
    input_tf = ft.TextField(
        label="새 계획 추가",
        value=input_value,
        expand=5,
        text_align=ft.TextAlign.LEFT,
        on_change=update_input,
    )

    def delete_plan(index):
        state.delete_my_made_plan(index)

    def append_plan(plan):
        set_selected_plan(plan)
        set_show_amount_input(True)
        set_chosen_plan(plan)

    making_plan_buttons = ft.Row(
        controls=[
            ft.Row(
                controls=[
                    ft.Button(plan, on_click=lambda _, plan=plan: append_plan(plan)),
                    ft.IconButton(
                        ft.Icons.DELETE_OUTLINE,
                        on_click=lambda e, index=index: delete_plan(index),
                    ),
                ]
            )
            for index, plan in enumerate(state.my_made_plan)
        ],
        wrap=True,
    )

    
    week_start = datetime.strptime(week_key, "%Y%m%d")
    week_start_m = week_start.strftime("%m")
    week_start_d = week_start.strftime("%d")
    week_end = week_start + timedelta(6)
    week_end_m = week_end.strftime("%m")
    week_end_d = week_end.strftime("%d")

    return ft.Column(
        controls=[
            ft.Text(str(week_start_m) + "/" + str(week_start_d) + "~" + str(week_end_m) + "/" + str(week_end_d) + "에 계획 추가", size=20),
            ft.Button("돌아가기", bgcolor="#8FFF3A", on_click=lambda _: page.navigate(f"/week_plan/{week_key}")),
            ft.Row(
                controls=[
                    ft.Text("문제집", expand=1, size=20, text_align=ft.TextAlign.CENTER),
                    ft.Button("수학", expand=1, on_click=lambda _: append_plan("수학 문제집 풀기")),
                    ft.Button("국어", expand=1, on_click=lambda _: append_plan("국어 문제집 풀기")),
                    ft.Button("영어", expand=1, on_click=lambda _: append_plan("영어 문제집 풀기")),
                    ft.Button("사회", expand=1, on_click=lambda _: append_plan("사회 문제집 풀기")),
                    ft.Button("과학", expand=1, on_click=lambda _: append_plan("과학 문제집 풀기")),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("책", expand=1, size=20, text_align=ft.TextAlign.CENTER),
                    ft.Button("한글", expand=1, on_click=lambda _: append_plan("한글책 읽기")),
                    ft.Button("영어", expand=1, on_click=lambda _: append_plan("영어책 읽기")),
                    ft.Text("", expand=3),
                    
                ]
            ),
            making_plan_buttons,
            how_much() if show_amount_input else ft.Container(),
            ft.Row(
                controls=[
                    ft.Button("기타", expand=1),
                    input_tf,
                    ft.IconButton(ft.Icons.ADD_ROUNDED, on_click=add_plan),
                ]
            ),
        ]
    )