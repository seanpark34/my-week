# from arrow import now
import flet as ft
from app_state import AppState
from datetime import datetime, timedelta

@ft.component
def Calendar(state: AppState, page: ft.Page):
    if not state.is_logged_in:
        return ft.Column(
            controls=[
                ft.Text("로그인이 필요합니다.", size=30),
                ft.Button("로그인", on_click=lambda e: page.navigate("/log_in"), bgcolor="#60FA41"),
            ]
        )
    
    month_color = {
        1: "#ff4646", 
        2: "#fb6b05", 
        3: "#ffa200", 
        4: "#ffd500", 
        5: "#becf22", 
        6: "#46ff4f",
        7: "#46fff6", 
        8: "#168eff", 
        9: "#0026ff", 
        10: "#8a46ff", 
        11: "#e95aff", 
        12: "#ff46a3"}
    day_color = {
        1: "#6a6a6a", 
        2: "#6a6a6a", 
        3: "#6a6a6a", 
        4: "#6a6a6a", 
        5: "#6a6a6a", 
        6: "#4693ff",
        7: "#fa0000"
    }

    today = datetime.now()
    day_num = today.weekday()+1
    month = today.strftime("%m")
    month_str = today.strftime("%b")

    if day_num == 7:
        day_num = 0
    else:
        day_num = today.weekday()+1

    week_start = today + timedelta(-day_num)

    def generate_week_key(offset: int):
        calendar_date = week_start + timedelta(days=offset)
        return calendar_date.strftime("%Y%m%d")
    
    def date_text(offset):
        calendar_date = week_start + timedelta(days=offset)
        color = day_color[calendar_date.isoweekday()]

        text = ft.Text(
            calendar_date.strftime("%d"),
            expand=1,
            size=20,
            color=color,
            text_align=ft.TextAlign.CENTER,
        )
        
        if calendar_date.date() == today.date():
            return ft.Container(
                ft.Container(
                    text,
                    bgcolor=ft.Colors.YELLOW,
                    shape=ft.BoxShape.CIRCLE,
                ),
                expand=1,
                
            )
        else:
            return text


    def open_week_plan(week_key):
        page.navigate(f"/week_plan/{week_key}")


    def generate_week(week_offset):
        day_offset = week_offset * 7
        week_key = generate_week_key(day_offset)
        days_list = [
            date_text(day_offset+days) for days in range(0,7)
        ]

        return [
            *days_list, 
            ft.IconButton(
                ft.Icons.SEARCH_ROUNDED,
                expand=1,
                on_click=lambda _: open_week_plan(week_key),
            ),
        ]

    weeks = [
        ft.Row(controls=generate_week(offset)) for offset in range(-1, 2)
    ]

    return ft.Column(
        controls=[
            ft.Text(str(month + " " + month_str), size=50, color=month_color[int(month)]),
            ft.Row(
                controls=[
                    ft.Text("Sun", expand=1, color=day_color[7], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Text("Mon", expand=1, color=day_color[1], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Text("Tue", expand=1, color=day_color[2], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Text("Wed", expand=1, color=day_color[3], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Text("Thu", expand=1, color=day_color[4], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Text("Fri", expand=1, color=day_color[5], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Text("Sat", expand=1, color=day_color[6], text_align=ft.TextAlign.CENTER, size=10),
                    ft.Icon(ft.Icons.SEARCH, color='#00000000', expand=1)
                ],
            ),
            *weeks,
        ]
    )