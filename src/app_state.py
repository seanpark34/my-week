from dataclasses import dataclass, field, fields, asdict
import json
import flet as ft
from datetime import date, datetime, timedelta

STORAGE_KEY = "my_week_"

@ft.observable
@dataclass
class AppState():
    page: ft.Page = field(default=None, repr=False)
    prefs: ft.SharedPreferences = field(default_factory=ft.SharedPreferences)

    # 앱 상태
    current_user_id: str = ""
    today = datetime.now()
    day_num = (today.weekday()+1) % 7
    week_start = today + timedelta(-day_num)
    week_start_ymd = week_start.strftime("%Y%m%d")
  
    # 앱 데이터
    users: list = field(default_factory=list)

    # 사용자 데이터
    nickname: str = "MyWeek 사용자"
    my_made_plan: list = field(default_factory=list)
    plans: dict = field(default_factory=dict)
    _week: int = 0 # 연속 진행한 주차 수
    _list_num : int = 1 # 계획에 부여할 고유 번호
    last_login: date = date.today() # 마지막 로그인 날짜의 다음주 일요일 날짜

    levels = {
        0: "루키(1/16)", 1: "스톤(2/16)", 2: "핑크(3/16)", 3: "오렌지(4/16)", 4: "브론즈(5/16)",
        5: "실버(6/16)", 6: "실버(6/16)", 7: "골드(7/16)", 8: "골드(7/16)", 9: "골드(7/16)",
        **dict.fromkeys(range(10, 15), "플래티넘(8/16)"),
        **dict.fromkeys(range(15, 20), "사파이어(9/16)"),
        **dict.fromkeys(range(20, 25), "루비(10/16)"),
        **dict.fromkeys(range(25, 30), "에메랄드(11/16)"),
        **dict.fromkeys(range(30, 35), "자수정(12/16)"),
        **dict.fromkeys(range(35, 40), "펄(13/16)"),
        **dict.fromkeys(range(40, 45), "다이아몬드(14/16)"),
        **dict.fromkeys(range(45, 52), "계획 마스터(15/16)"),
        **dict.fromkeys(range(52, 10000), "계획 왕(16/16)"),
    }

    @property
    def is_logged_in(self) -> bool:
        return self.current_user_id != ""

    @property
    def plan_week(self) -> int:
        return self._plan_week

    @plan_week.setter
    def plan_week(self, value: int):
        self._plan_week = value
        self.page.run_task(self._save_user_data_async, "plan_week", value)


    @property
    def week(self) -> int:
        return self._week

    @week.setter
    def week(self, value: int):
        self._week = value
        self.page.run_task(self._save_user_data_async, "week", value)

    @property
    def list_num(self) -> int:
        self._list_num += 1
        self.page.run_task(self._save_user_data_async, "list_num", self._list_num)

        return self._list_num

    async def load_state_async(self):
        if self.page is not None:
            saved_users = await self.prefs.get(f"{STORAGE_KEY}_users")
            
            if saved_users is not None:
                self.users = json.loads(saved_users)

    def add_user(self, user):
        self.users.append(user)
        if self.page is not None:
            # 백그라운드 태스크로 비동기 저장 실행 (await 필요 없음)
            self.page.run_task(self._save_users_async, self.users)
        print(f"User added and saved to SharedPreferences: {user}")

    async def load_user_data(self):
        print(f"load_user_data")
        if self.page is not None and self.current_user_id:
            saved_nickname = await self.prefs.get(f"{STORAGE_KEY}_{self.current_user_id}_nickname")
            saved_my_made_plan = await self.prefs.get(f"{STORAGE_KEY}_{self.current_user_id}_my_made_plan")
            saved_plans = await self.prefs.get(f"{STORAGE_KEY}_{self.current_user_id}_plans")
            saved_week = await self.prefs.get(f"{STORAGE_KEY}_{self.current_user_id}_week")
            saved_list_num = await self.prefs.get(f"{STORAGE_KEY}_{self.current_user_id}_list_num")
            saved_last_login = await self.prefs.get(f"{STORAGE_KEY}_{self.current_user_id}_last_login")

            if saved_nickname is not None:
                self.nickname = saved_nickname
            if saved_my_made_plan is not None:
                self.my_made_plan = json.loads(saved_my_made_plan)
            if saved_plans is not None:
                self.plans = json.loads(saved_plans)
            if saved_week is not None:
                self._week = int(saved_week)
            if saved_list_num is not None:
                self._list_num = int(saved_list_num)
            if saved_last_login is not None:
                self.last_login = date.strptime(saved_last_login, "%Y%m%d%H")

    def set_logged_in(self, user):
        self.current_user_id = user["id"]
        print(f"Logged in as: {self.current_user_id}")

    def save_nickname(self, nickname: str):
        self.nickname = nickname
        if self.page is not None:
            self.page.run_task(self._save_user_data_async, "nickname", nickname)

    def add_my_made_plan(self, plan):
        self.my_made_plan.append(plan)
        if self.page is not None:
            self.page.run_task(self._save_user_data_async, "my_made_plan", json.dumps(self.my_made_plan))

    def delete_my_made_plan(self, plan):
        self.my_made_plan.pop(plan)
        if self.page is not None:
            self.page.run_task(self._save_user_data_async, "my_made_plan", json.dumps(self.my_made_plan))

    def add_plan_of_week(self, week_key, new_plan):
        new_plan["num"] = self.list_num
        self.plans_for_selected_week(week_key).append(new_plan)
        self.save_plans()

    def save_plans(self):
        if self.page is not None: 
            print(f"saving plans", self.plans)
            self.page.run_task(self._save_user_data_async, "plans", json.dumps(self.plans))

    def save_last_login(self):
        today = datetime.now()
        print("saving last login time")
        self.page.run_task(self._save_user_data_async, "last_login", today.strftime("%Y%m%d%H"))
    
    # 비동기 저장용 내부 도우미 함수
    async def _save_users_async(self, value: list):
        print(f"Saving users: {value}")
        await self.prefs.set(f"{STORAGE_KEY}_users", json.dumps(value))

    async def _save_user_data_async(self, key: str, value: any):
        print(f"Saving user data: {key} = {value}")
        await self.prefs.set(f"{STORAGE_KEY}_{self.current_user_id}_{key}", value)


    def plans_for_selected_week(self, week_key: str) -> list:
        plans_of_the_week = self.plans.get(week_key)
        if plans_of_the_week is None:
            self.plans[week_key] = []
            plans_of_the_week = self.plans[week_key]
        return plans_of_the_week
