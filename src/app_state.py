from dataclasses import dataclass, field
import flet as ft

@ft.observable
@dataclass
class AppState():
    cart: list = field(default_factory=list)
    cart_count: int = 0
