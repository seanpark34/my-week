import flet as ft
from app_state import AppState





@ft.component
def Guide(state: AppState, page: ft.Page):

    guide_texts, set_guide_texts = ft.use_state(ft.Column(controls=[]))
    clicked_button, set_clicked_button = ft.use_state("")


    def show_app_definition():
        set_clicked_button("app")
        set_guide_texts(
             ft.Column(
                controls=[
                    ft.Text("MyWeek는 쉽게 일주일 단위로 계획을 세우고 실천할 수 있게 도와주는 앱입니다.", size=12),
                    ft.Text("", size = 5),
                    ft.Text("일주일 단위로 계획을 세우면 좋은점이 많아요!", size=12),
                    ft.Text("1. 시간이 정해져있지 않아 혼자서 시간을 잘 활용할 수 있어요!", size=12),
                    ft.Text("2. 한 주 안에서 밀리면 다음날 더 열심히 할 수 있어요!", size=12),
                    ft.Text("3. 반대로 한 주 안에서 빨리 할 일을 끝내면 놀 수 있어요!", size=12),
                    ft.Text("4. 오늘 할 일을 잘 하지 못해도 내일이 있기 때문에 안심할 수 있어요!", size=12),
                    ft.Text("5. 지난주에 무엇을 했는지 돌아보고 더 좋은 계획을 세울 수 있어요!", size=12),
                    ft.Text("", size = 5),
                    ft.Text("MyWeek에서 쉽게 계획을 세우고 실천해 일주일 단위로 계획을 세우는 것의 공부 효과를 느껴보세요!", size=12),
                    # ft.Button("돌아가기", bgcolor="#60FA41", on_click=guide_page)
                ]
            )
        )

    def show_profile_definition():
        set_clicked_button("profile")
        set_guide_texts(
            ft.Column(
                controls=[
                    ft.Text("프로필에는 닉네임, 주, 트로피가 있습니다.", size=12),
                    ft.Text("닉네임은 닉네임 아래의 닉네임 변경 버튼을 눌러 바꿀 수 있습니다", size = 12),
                    ft.Text("", size=5),
                    ft.Text("Week는 일요일 자정 이후 다음 로그인 했을 때 할 일을 다했으면 1이 올라갑니다.", size=12),
                    ft.Text("(할 일이 하나도 없는 경우에는 올라가지 않습니다.)", size=12),
                    ft.Text("주별로 트로피를 주는데, 0주를 했을 때는 루키이고 트로피가 없지만 1주, 2주 성공할 때마다 트로피 레벨이 올라갑니다.", size=12),
                    ft.Text("물론 트로피 레벨이 올라가지 않는 주도 있습니다.", size=12),
                    ft.Text("열심히 학습해 모든 트로피를 획득하세요!", size=12),
                ]
            )
        )

    def show_add_plan_definition():
        set_clicked_button("add_plan")
        set_guide_texts(
            ft.Column(
                controls=[
                    ft.Text("오른쪽 상단 달력모양 버튼을 누른 후 원하는 주의 오른쪽에 있는 돋보기 버튼을 누르면 그 주의 계획을 볼 수 있습니다.", size=12),
                    ft.Text("", size=5),
                    ft.Text("+버튼을 누르면 할 일을 추가할 수 있는데,", size=12),
                    ft.Text("기본적으로 문제집 풀기와 책 읽기가 있고 그 이외의 할 일들은 기타 버튼 옆에 타자로 친 후 +버튼을 누르면 나만의 할 일을 추가할 수 있습니다.", size=12),
                    ft.Text("그 후 버튼을 누르고 수량과 단위를 설정하면 계획이 추가됩니다.", size=12),
                    ft.Text("", size=5),
                    ft.Text("다시 달력 버튼을 누르고 달력화면으로 돌아가서 다른 주의 오른쪽에 있는 돋보기 버튼을 누르면 다른 주의 계획도 볼 수 있습니다.", size=12),
                ]
            )
        )

    def show_done_plan_definition():
        set_clicked_button("done_plan")
        set_guide_texts(
            ft.Column(
                controls=[
                    ft.Text("오른쪽 상단 달력모양 버튼을 누른 후 원하는 주의 오른쪽에 있는 돋보기 버튼을 누르면 그 주의 계획을 볼 수 있습니다.", size=12),
                    ft.Text("+버튼을 눌러서 할 일을 추가한 뒤(자세한 내용은 '계획 추가'를 참고해 주세요.)", size = 12),
                    ft.Text("그 계획 왼쪽에 있는 돋보기 버튼을 누르면 얼마나 했는지 볼 수 있고 +/- 버튼으로 올렸다 내렸다 할 수 있습니다.", size=12),
                    ft.Text("한 만큼 체크했으면 돌아가기 버튼을 눌러 다시 한 주의 계획을 볼 수 있고 할일 삭제 버튼을 누르면 계획을 삭제할 수 있습니다.", size=12),
                    ft.Text("", size=5),
                    ft.Text("할 일은 물론 그 주에 끝내면 가장 좋지만 밀렸을 경우 다음주까지 기회가 주어집니다.", size=12),
                    ft.Text("하지만 다음주에 다 했다고 Week가 올라가지는 않습니다.", size=12),
                ]
            )
        )

    return ft.Column(
        controls=[
            ft.Text("📖앱 사용 가이드", size=25),
            ft.Text("", size = 5),
            ft.Column(
                controls=[
                    ft.Text("안녕하세요! MyWeek를 사용해주셔서 감사합니다.", size=15),
                    ft.Text("궁금한 것을 눌러주세요.", size=15),
                    ft.Row(
                        controls=[
                            ft.Button("앱 설명", 
                                    bgcolor = ft.Colors.BLUE if clicked_button=="app" else None,
                                    on_click=lambda _: show_app_definition()),
                            ft.Button("프로필 설명", 
                                    bgcolor = ft.Colors.BLUE if clicked_button=="profile" else None,
                                    on_click=lambda _: show_profile_definition()),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Button("계획 추가", 
                                    bgcolor = ft.Colors.BLUE if clicked_button=="add_plan" else None,
                                    on_click=lambda _: show_add_plan_definition()),
                            ft.Button("계획 완료", 
                                    bgcolor = ft.Colors.BLUE if clicked_button=="done_plan" else None,
                                    on_click=lambda _: show_done_plan_definition()),
                        ]
                    ),
                    guide_texts        
                        ]
                    )
                ]
            )